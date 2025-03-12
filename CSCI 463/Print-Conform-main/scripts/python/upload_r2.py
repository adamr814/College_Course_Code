# PrintConform Upload to Cloudflare R2 Script
# Version: 0.6
# Purpose: Uploads a specified file to Cloudflare R2.
### Inputs: argv1:filepath
### External Interfaces: Amazon S3 API
### Outputs: Login yes or no.
# Author: Brandon Veen
# Creation Date: 3-10-2024
# Modification History:
### 3-10-2024: Initial Version Created
### 5-3-2024: Script modified to function with other modules.

import sys
import os
import subprocess
import tkinter
from tkinter import filedialog
from io import BytesIO
import connect_r2

def upload(file_path, pc_user, order_id):
    #bucket_name = 'pcuser\\' + pc_user + '\\' + order_id
    bucket_name = 'pcuser'
    print(bucket_name)
    head, tail = os.path.split(file_path.name)
    #object_name = '1068253/test2.jpg'
    object_name = '{0}/{1}/{2}'.format(pc_user, order_id, tail) 
    print (object_name)
    s3 = connect_r2.connect()
    with open(file_path.name, "rb") as f:
        s3.upload_fileobj(f, bucket_name, object_name)
    s3.close()

def select_file():
    #Grab File to Upload
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfile()
    print("File selected:" + file_path.name)
    return(file_path)

#Main Method
def main():
    file_path = select_file()
    pc_user = str(2)
    order_id = str(512188)
    upload(file_path, pc_user, order_id)

if __name__ == "__main__":
    main()