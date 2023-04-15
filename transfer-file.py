import pysftp
import tkinter as tk
from tkinter import filedialog
import random
import string

def upload_file():
    # Opens a dialog box to choose a file
    local_file_path = filedialog.askopenfilename()
    
    # If no file has been selected, exit the function
    if not local_file_path:
        return
    
    # Configure the SFTP connection with an SSH certificate
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None # Ignore authentication errors    
    with pysftp.Connection('IP.OF.YOUR.SERVER', username='USERNAME', password='PASSWORD', cnopts=cnopts) as sftp:

    # If you would to use a ssh certificat for logging, replace line 18 for this :
    # private_key_path = "path/of/your/private/ssh.key"
    # with pysftp.Connection('IP.OF.YOUR.SERVER', username='USERNAME', private_key=private_key_path, cnopts=cnopts) as sftp:
  
        # Upload your file
        remote_path = remote_path_entry.get() + local_file_path.split('/')[-1]
        sftp.put(local_file_path, remote_path)
    
    # Generates the link to view the hosted file
    server_url = "https://domaine.name/directory/path" # path where you want to store your uploaded files
    file_name = local_file_path.split('/')[-1]
    file_url = server_url + file_name
    
    # Show success message pop-up when the file was uploaded
    #tk.messagebox.showinfo("Success", f"File uploaded successfully\n\nURL: {file_url}")
    
    # Display the link in the text field and copy it to the clipboard
    file_url_entry.delete(0, tk.END)
    file_url_entry.insert(0, file_url)
    root.clipboard_clear()
    root.clipboard_append(file_url)

# Setup Graphic Interface
root = tk.Tk()
root.title("Transfer File")
root.geometry("400x150")
root.resizable(False, False)
# App icon
root.iconbitmap('cloud.ico')

# Fields for the remote path
remote_path_frame = tk.Frame(root)
remote_path_frame.pack(pady=10)

remote_path_label = tk.Label(remote_path_frame, text="Remote Path:")
remote_path_label.pack(side=tk.LEFT)

remote_path_entry = tk.Entry(remote_path_frame)
remote_path_entry.pack(side=tk.LEFT)

remote_path_entry.insert(0, "/var/www/html/") # by default

# Fields for link generated
file_url_frame = tk.Frame(root)
file_url_frame.pack(pady=10)

file_url_label = tk.Label(file_url_frame, text="File URL:")
file_url_label.pack(side=tk.LEFT)

file_url_entry = tk.Entry(file_url_frame, width=40)
file_url_entry.pack(side=tk.LEFT)

# Button for upload file
upload_button = tk.Button(root, text="Upload your file", command=upload_file)
upload_button.pack(pady=10)

root.mainloop()
