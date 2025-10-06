#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os, sys

# Optional: use tqdm for a nice progress bar; fall back to no-op if not installed
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(*args, **kwargs):
        class DummyTQDM:
            def update(self, n=1): pass
            def close(self): pass
            def __enter__(self): return self
             def __exit__(self, exc_type, exc, tb): pass
        return DummyTQDM()

def backupToZip(folder):
    #Backup the entire contents of "folder" into a Zip file
    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the filename this code should use based on what file already exists.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file
    print(f"Creating {zipFilename}...")
    backupZip = zipfile.ZipFile(zipFilename, "w", compression=zipfile.ZIP_DEFLATED)

    # Build a flat list of files so tqdm has a known 'total'
    files_to_zip = []
    newBase = os.path.basename(folder) + "_"
    for root, _, files in os.walk(folder):
        for file in files:
            # Don't re-zip previous backups created by this script
            if file.startswith(newBase) and file.endswith(".zip"):
                continue
            files_to_zip.append(os.path.join(root, file))
    total_bytes = sum(os.path.getsize(p) for p in files_to_zip)
    print(f"Total: {total_bytes} bytes")

    for root, _, files in os.walk(folder):
        arcdir = os.path.relpath(root, start=folder)
        if arcdir != ".":
            backupZip.write(root, arcdir)
    with tqdm(total=total_bytes, unit="B", unit_scale=True,  desc="Zipping") as pbar:
        for path in files_to_zip:
            arcname = os.path.relpath(path, start=folder)
            backupZip.write(path, arcname)
            pbar.update(os.path.getsize(path))

    backupZip.close()
    print("Done")

if __name__ == '__main__':
    # Use CLI arg if provided, else prompt
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Enter the folder path to backup: ").strip()
    backupToZip(target)
