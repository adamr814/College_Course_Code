import os
from dotenv import load_dotenv
import mysql.connector

#Load environment variables from .env file in folder directory
current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_file = os.path.join(current_dir, 'SQLserver.env')
load_dotenv(dotenv_file)

hostname = os.getenv("MYSQL_HOST")
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

#Automatically use these variables to connect to OptiChart Server
try:
    connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database)
    print("Connection successful!")

except mysql.connector.Error as err:
    print(f"Connection failure: {err}")

finally:
    if connection:
        connection.close()
    print("Connection closed")
