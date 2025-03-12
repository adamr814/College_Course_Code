# PrintConform Password Salt Generator
# Version: 1.0
# Purpose: Generates a random salt
### Inputs: argv[1]: 'js' (Optional)
### Outputs: 16 Character Randomized Salt String with optional Javascript flush
# Author: Brandon Veen
# Creation Date: 5-2-2024
# Modification History:
### 5-2-2024: Created

import sys
import secrets

#Generate Salt Method: Generates a 16 Character (12.3 bytes) randomized salt String
def generate_salt():
    return secrets.token_urlsafe(12)

#Main Method: Prints the salt string, if a 'js' argument is passed at runtime also flushes the stdout.
def main():
    #Generate Salt
    salt = generate_salt()

    #Print Output
    print(salt)

    #Flush output if called by JS.
    if len(sys.argv) == 2 and sys.argv[1] == 'js':
            # Flush Standard Output (for JS)
            sys.stdout.flush()        

if __name__ == '__main__':
    main()