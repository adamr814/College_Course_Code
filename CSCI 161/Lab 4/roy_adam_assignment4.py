'''
Adam Roy
Assignment 4
CSCI 161
'''

import os

def count_char(sent):
    string = sent.strip()
    print('*** There are', len(string), 'characters ***')
    
def count_word(sent):
    word = sent.split()
    print('*** There are', len(word), 'words in this string ***')
    
def rev_sentence(sent):
    string = sent[::-1]
    print(string)

def main():
    
    sent = str(input('Please enter a sentence: '))
    print('\nYou entered: ', sent)
    select = None
    
    while select != 'q':
        print('\nMENU\n')
        print('c - Number of non-whitespace characters')
        print('w - Number of words')
        print('r - Reverse the order of words in the sentence')
        print('q - Quit')
        select = str(input('\n\nChoose an option: ').lower())
        
        if select == 'c':
            count_char(sent)
            
            
        elif select == 'w':
            count_word(sent)
            
            
        elif select == 'r':
            rev_sentence(sent)
                
        elif select != 'q':
            print('\nInvalid, Please try again\n')
            continue
        continue
     
    print('\nThank you, Goodbye!')
    os._exit(0)                    
    
    
main()