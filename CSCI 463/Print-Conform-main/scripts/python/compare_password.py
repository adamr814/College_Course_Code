# PrintConform Password Check Script
# Version: 0.5
# Purpose: Compares the input password to the saved hash in the MySQL database for a given user.
### Inputs: argv1:uid, argv2:password
### External Interfaces: MySQL Database (salt & hashed password)
### Outputs: Login yes or no.
# Author: Brandon Veen
# Creation Date: 5-2-2024
# Modification History:
### 5-2-2024: Initial Version Created

import sys
import hash
import connect_db

def grab_hash(uid):
    #Connect to MySQL
    conn = connect_db.connect_db()
    cursor = conn.cursor()

    #Define query to grab user's salt.
    query = "SELECT user_password, uid FROM pcuser WHERE uid = " + uid

    #Obtain users salt from MySQL
    cursor.execute(query)
    for (result, uid) in cursor:
        #print("{} : {}".format(uid, result))
        hash = result

    #Close Connection
    cursor.close()
    conn.close()

    #Return hash
    return(hash)

def main():
    #Check for command line arguments
    if len(sys.argv) != 3:
        print("Program requires argv(1): Hashable Password, argv(2): userID")
        sys.exit(0)

    #Hash the user's inputted password
    userinput = hash.generate(sys.argv[1], sys.argv[2])
    #Obtain the saved hash in MySQL database
    storedhash = grab_hash(sys.argv[2])

    #Compare the two hashed passwords
    if (userinput == storedhash):
        print("True")
    else:
        print("False")

    #Flush the stdout.
    sys.stdout.flush()

if __name__ == '__main__':
    main()
