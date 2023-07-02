# File Transfer with SFTP

This script allows you to upload a file to a remote server using the Secure File Transfer Protocol (SFTP) and generate a link to access the uploaded file.
(tested for windows 10)

## Prerequisites

Before running this script, make sure you have the following:

- Python 3 installed
- `pysftp` library installed (`pip install pysftp`)
- `tkinter` library installed (`sudo apt-get install python3-tk` on Debian-based systems)

## Usage

1. Update the following information in the script:

   - Replace `'IP.OF.YOUR.SERVER'` with the IP address or hostname of your SFTP server.
   - Replace `'USERNAME'` and `'PASSWORD'` with your SFTP server credentials.
   - Modify the `remote_path_entry.insert(0, "/var/www/html/")` line to set the default remote path where you want to upload your files.

2. Run the script:
```
python3 file_transfer.py
```
3. The script will open a file dialog box. Choose the file you want to upload.

4. After the file is uploaded, a link to access the file will be generated. The link will be displayed in the "File URL" field and copied to your clipboard.

(tested for windows 10)
