import ftplib
import os

# FTP credentials
FTP_HOST = "ftp.wuk.naf.temporary.site"
FTP_USER = "Stephen"
FTP_PASS = "Splash2024$$"
FTP_PORT = 21
FTP_PATH = "/home1/wuknafte/jukebots.site/stephen"

def upload_file_to_ftp(local_file_path, remote_file_name):
    try:
        # Establish FTP connection
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_PATH)

        # Open the local file and upload
        with open(local_file_path, 'rb') as file:
            ftp.storbinary(f"STOR {remote_file_name}", file)

        # Quit FTP connection
        ftp.quit()
        print(f"File '{remote_file_name}' successfully uploaded to FTP server.")
    except ftplib.all_errors as e:
        print(f"Failed to upload {remote_file_name} due to: {e}")

# Directory with the charts
local_dir_path = './Charts/Dividend_Kings/'

# Loop through all .png files in the directory and upload them
for file_name in os.listdir(local_dir_path):
    if file_name.endswith('.png'):
        local_file_path = os.path.join(local_dir_path, file_name)
        remote_file_name = file_name
        upload_file_to_ftp(local_file_path, remote_file_name)

