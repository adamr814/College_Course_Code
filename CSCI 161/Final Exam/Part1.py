'''
Adam Roy
FINAL PROGRAM Part 1
CSCI 161
'''
#ver 1.3
import re

print('''
Enter a passwords between 6-12 characters seperated by commas:
At least 1 lowercase
At least 1 uppercase
At least 1 number
At least 1 special character
''')
passwords = input('- ')
passwords = passwords.split(',')
valid_passwords = []
i = 0
for i in range(0, len(passwords)):
    if not re.search('[a-z]', passwords[i]):
        continue
    elif not re.search('[A-Z]', passwords[i]):
        continue
    elif not re.search('[0-9]', passwords[i]):
        continue
    elif not re.search('[$#@]', passwords[i]):
        continue
    elif (len(passwords[i]) < 6 or len(passwords[i]) > 12):
        continue
    else:
        print('Valid Passwords: ', passwords[i])