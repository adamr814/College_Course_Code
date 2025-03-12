# PrintConform Connect R2 - Python
# Version: 1.0
# Purpose: Used to connect to the Cloudflare R2 Server via the Amazon Compatibility SDK boto3
# Instructions: File should be kept out of root, and only be accessable from PHP user (CHMOD ???).
# In the python program that needs to upload or download from R2: "import connect_r2" and close the connection via s3.close().
# Author: Brandon Veen
# Creation Date: 5-2-2024
# Modification History:
### 5-2-2024 - First version completed.

#import botocore
import boto3
#from sshtunnel import SSHTunnelForwarder

def connect():
    #Open the S3 connection
    s3 = boto3.client(
            service_name = 's3',
            endpoint_url = 'https://b02439ffa32c04d1cc77e1b04b04f6d7.r2.cloudflarestorage.com/printconform',
            aws_access_key_id = 'c131131fecbf77704a7a0808f62e4fe6',
            aws_secret_access_key = '03f7a34a7fbf62ea3029c10826cd71930fe2869b88a7c3433b9cfbcee5f5fe18',
            region_name = 'auto',
    )

    #try: 
    #except mysql.connector.Error as err:
    #    print(err)
    #    s3 = -1
    
    #Return connection to calling function.
    return(s3)
