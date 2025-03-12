# PrintConform Connect DB - Python
# Version: 1.0
# Purpose: Used to connect to the PrintConform database. 
# Instructions: File should be kept out of root, and only be accessable from PHP user (CHMOD ???).
# In the python program that needs to call the MySQL database: "import connect-db" and close the connection via conn.close().
# Author: Brandon Veen
# Creation Date: 5-2-2024
# Modification History:
### 5-2-2024 - First version completed.

import mysql.connector
#from sshtunnel import SSHTunnelForwarder

def connect_db():
    #Define config
    config = {
        'user': 'printconform',
        'password': 'FUtBt!4Oqs',
        'host': 'mysql.printconform.com',
        'database': 'printconform',
        'raise_on_warnings': True
    }
    #Open Connection to MySQL
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(err)
        conn = -1
    
    #Return connection to calling function.
    return(conn)
