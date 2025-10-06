# backup /users/ryanduggan/python to ZIP

import zipfile, os

def backupToZip(folder):
    #Back up the entire contents of "folder" into a Zip file
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
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding {foldername}...")
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue    # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done")
    from datetime import datetime
    print("Backup completed at:", datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

backupToZip("/users/ryanduggan/python")

#ChatGPT helped me with the timestamp requirement of this assignment.
