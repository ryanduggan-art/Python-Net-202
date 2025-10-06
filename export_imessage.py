#!/usr/bin/env python3
"""
Export iMessage conversation to a .txt file.

Usage:
  python export_imessage.py <search_string> output.txt

search_string can be (partial) phone number, email, or display name.
"""
import sqlite3, shutil, sys, os
from datetime import datetime, timedelta
import tempfile

MAC_EPOCH = datetime(2001, 1, 1)

def mac_time_to_datetime(mac_time):
    if mac_time is None:
        return None
    try:
        t = float(mac_time)
    except Exception:
        return None
    if t > 1e14:
        t = t / 1e9
    elif t > 1e11:
        t = t / 1e6
    elif t > 1e9:
        t = t / 1e3
    try:
        return MAC_EPOCH + timedelta(seconds=t)
    except Exception:
        return None

def copy_db(src_path):
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"DB not found at {src_path}")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    tmp.close()
    shutil.copy2(src_path, tmp.name)
    return tmp.name

def find_chats(conn, search):
    """
    Return list of (chat_id, display_name, guid) that match the search term
    """
    cur = conn.cursor()
    q = """
    SELECT DISTINCT chat.ROWID AS chat_id,
           COALESCE(chat.display_name, '') AS display_name,
           COALESCE(chat.guid, '') AS guid
    FROM chat
    LEFT JOIN chat_handle_join chj ON chat.ROWID = chj.chat_id
    LEFT JOIN handle h ON h.ROWID = chj.handle_id
    WHERE h.id LIKE ?
       OR chat.display_name LIKE ?
       OR chat.guid LIKE ?
    ORDER BY (chat.display_name IS NULL), chat.display_name
    """
    term = f"%{search}%"
    cur.execute(q, (term, term, term))
    return cur.fetchall()

def export_chat(conn, chat_rowid, out_path, copy_attachments=True):
    """
    Export messages from a given chat ROWID to out_path.
    Optionally copies attachments into '<out_path>_attachments/' and
    references them by filename in the text export.
    """
    cur = conn.cursor()
    q = """
    SELECT
        m.ROWID AS msg_id,
        m.date,
        m.is_from_me,
        m.text,
        m.associated_message_type,
        m.associated_message_guid,
        h.id AS handle_id,
        a.filename AS att_filename,
        a.transfer_name AS att_transfer_name
    FROM message m
    JOIN chat_message_join cmj ON cmj.message_id = m.ROWID
    JOIN chat c ON c.ROWID = cmj.chat_id
    LEFT JOIN handle h ON m.handle_id = h.ROWID
    LEFT JOIN message_attachment_join maj ON maj.message_id = m.ROWID
    LEFT JOIN attachment a ON a.ROWID = maj.attachment_id
    WHERE c.ROWID = ?
    ORDER BY m.date ASC, a.ROWID ASC
    """
    cur.execute(q, (chat_rowid,))

    # Group by message
    messages = {}
    for row in cur.fetchall():
        msg_id = row["msg_id"]
        d = messages.setdefault(msg_id, {
            "date": row["date"],
            "is_from_me": row["is_from_me"],
            "text": row["text"],
            "assoc_type": row["associated_message_type"],
            "assoc_guid": row["associated_message_guid"],
            "handle": row["handle_id"],
            "attachments": []
        })
        if row["att_filename"] or row["att_transfer_name"]:
            d["attachments"].append({
                "filename": row["att_filename"],
                "transfer_name": row["att_transfer_name"]
            })

    # Where original attachments live
    messages_base = os.path.expanduser("~/Library/Messages")
    att_out_dir = os.path.splitext(out_path)[0] + "_attachments"
    if copy_attachments and not os.path.exists(att_out_dir):
        os.makedirs(att_out_dir, exist_ok=True)

    # Map Tapbacks
    tapbacks = {
        2000: "loved",
        2001: "liked",
        2002: "disliked",
        2003: "laughed at",
        2004: "emphasized",
        2005: "questioned"
    }

    def pretty_timestamp(mac_date_raw):
        dt = mac_time_to_datetime(mac_date_raw)
        return dt.strftime("%Y-%m-%d %H:%M:%S") if dt else str(mac_date_raw)

    def copy_attachment(src_rel, transfer_name, idx):
        # src_rel may be a relative path like "Attachments/xx/yy/file.jpg"
        if not src_rel:
            return None
        src = src_rel if os.path.isabs(src_rel) else os.path.join(messages_base, src_rel)
        if not os.path.exists(src):
            return None
        # create a readable, collision-safe name
        base = transfer_name or os.path.basename(src)
        safe = f"{idx:03d}_" + base
        dst = os.path.join(att_out_dir, safe)
        try:
            shutil.copy2(src, dst)
            return os.path.relpath(dst, os.path.dirname(out_path))
        except Exception:
            return None

    with open(out_path, "w", encoding="utf-8") as f:
        for i, msg_id in enumerate(sorted(messages.keys())):
            m = messages[msg_id]
            ts = pretty_timestamp(m["date"])
            sender = "Me" if m["is_from_me"] == 1 else (m["handle"] or "Unknown")

            # Decide body text
            body = (m["text"] or "").replace("\r\n", "\n").replace("\r", "\n").strip()

            # Render Tapbacks (reactions) when text is empty but associated fields exist
            if not body and m["assoc_type"] in tapbacks and m["assoc_guid"]:
                body = f"[{tapbacks[m['assoc_type']]} a message]"

            # If still empty and there are attachments, list them
            att_refs = []
            if m["attachments"]:
                for j, att in enumerate(m["attachments"], start=1):
                    if copy_attachments:
                        copied = copy_attachment(att["filename"], att["transfer_name"], j)
                        if copied:
                            att_refs.append(copied)
                    # fallback: show original path/transfer name
                    if not att_refs and (att["transfer_name"] or att["filename"]):
                        att_refs.append(att["transfer_name"] or att["filename"])
                if not body:
                    body = "[attachment] " + ", ".join(att_refs) if att_refs else "[attachment]"

            if not body:
                body = "[non-text message]"

            f.write(f"[{ts}] {sender}: {body}\n\n")

    return out_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python export_imessage.py <search_string> output.txt")
        sys.exit(1)
    search = sys.argv[1]
    out_file = sys.argv[2]

    db_path = os.path.expanduser('~/Library/Messages/chat.db')
    try:
        tmpdb = copy_db(db_path)
        conn = sqlite3.connect(tmpdb)
        conn.row_factory = sqlite3.Row
    except Exception as e:
        print("Failed to copy/open Messages DB:", e)
        print("Make sure you have Full Disk Access and that the DB exists at ~/Library/Messages/chat.db")
        sys.exit(2)

    try:
        matches = find_chats(conn, search)
        if not matches:
            print(f"No chats found matching '{search}'. Try a different search (phone number, email, or display name).")
            return
        if len(matches) > 1:
            print("Multiple chats found. Exporting the first match. (If wrong, re-run with a more specific search.)")
            for i, (chat_id, display_name, guid) in enumerate(matches, 1):
                print(f"{i}. chat_id={chat_id}, display_name='{display_name}', guid='{guid}'")
        else:
            chat_id, display_name, guid = matches[0]
            print(f"Found chat: chat_id={chat_id}, display_name='{display_name}', guid='{guid}'")

        chat_id = matches[0][0]
        exported = export_chat(conn, chat_id, out_file)
        print("Exported to:", exported)
    finally:
        conn.close()
        os.unlink(tmpdb)

if __name__ == '__main__':
    main()
