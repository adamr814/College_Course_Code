# PrintConform Password Hashing Python Script
# Version: 0.5
# Purpose: Script used for generating a hashed password based on the given string input.
### Inputs: argv1:PlaintextPassword, argv2:UserID
### External Interfaces: MySQL Query (for grabbing salt)
### Outputs: SHA3-512 Salted Password in Hexidecimal
# Author: Brandon Veen
# Creation Date: 5-2-2024
# Modification History:
### 5-2-2024: Initial Version Created

import sys
import hashlib
import connect_db

def generate(password, uid):
    #Connect to MySQL
    conn = connect_db.connect_db()
    cursor = conn.cursor()

    #Define query to grab user's salt.
    query = "SELECT salt, uid FROM pcuser WHERE uid = " + uid

    #Obtain users salt from MySQL
    cursor.execute(query)

    for (result, uid) in cursor:
        #print("{} : {}".format(uid, result))
        salt = result
    
    #Generate sha3_512 Hash of Password (sys.argv[1]) + salt
    hash = hashlib.sha3_512()
    hash.update(password.encode('utf-8'))
    hash.update(salt.encode('utf-8'))
    
    #Digest into Hex values
    password = hash.hexdigest()
    
    #Close Connection
    cursor.close()
    conn.close()

    #Return the hashed password
    return(password)


#Main Program (meant for calling via Javascript)
def main():
    #Check that proper command line arguments are being provided.
    if len(sys.argv) != 3:
        print("Program requires argv(1): Hashable Password, argv(2): userID")
        sys.exit(0)

    #Call generate method and pass command line arguments
    hashed = generate(sys.argv[1], sys.argv[2])

    #Flush password to sys.out.
    print(hashed)
    sys.stdout.flush()

if __name__ == '__main__':
    main()