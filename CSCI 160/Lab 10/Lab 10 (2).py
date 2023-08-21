import random
import os
 
def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print() 
 
def check_win(values):
    for char in values:
        if char == '*':
            return False
    return True    
 
def hangman_game(word):
    word_display = []
    correct_letters = []
    incorrect = []
    
    lives = 0
    dif = input("\nChoose a difficulty, 'easy' 'medium' or 'hard': ")
    while lives == 0:
        if dif == 'easy':
            lives = 9
        elif dif == 'medium':
            lives = 7
        elif dif == 'hard':
            lives = 5
        else:
            print('Invalid difficulty selected')
            dif = input("\nchoose a difficulty, 'easy' 'medium' or 'hard'")    
 
    for char in word:
        if char.isalpha():
            word_display.append('*')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)
          
    while True:
 
        print_word(word_display)            
        print()
        print("Incorrect characters : ", incorrect)
        print()
 
        inp = input("Enter a character = ")
        if len(inp) != 1:
            print("Wrong choice!! Try Again")
            continue
        if not inp[0].isalpha():
            print("Wrong choice!! Try Again")
            continue   
        if inp.upper() in incorrect:
            print("Already tried!!")
            continue   
 
        if inp.upper() not in correct_letters:
            incorrect.append(inp.upper())
            lives -= 1
            print(lives, 'incorrect guess/es remaining')
             
            if lives == 0:
                print()
                print("\tGAME OVER!!!")
                print("The word is :", word.upper())
                print()
                print('Would you like to play again? yes/no')
                
                eog = str(input())
                
                if eog == 'yes':
                    hangman_game(word)
                elif eog == 'no':
                    print('Thanks for playing')
                    quit()
                else:
                    print('Invalid')
                    quit()
 
        else:
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
       
            if check_win(word_display):
                print("\tCongratulations! ")
                print("The word is :", word.upper())
                print()
                print('Would you like to play again? yes/no')
                
                eog = str(input())
                
                if eog == 'yes':
                    hangman_game(word)
                elif eog == 'no':
                    print('Thanks for playing')
                    quit()
                else:
                    print('Invalid')
                    quit()
     
 
if __name__ == "__main__":
 
    f = 'words.txt'
    if not os.path.isfile (f):
        print('\nInput file is missing')
        os._exit(0)
        
    f = open(f, 'r')
    i = 0
    lines = f.readlines()
    dataset = {}
    for i in range(0, len(lines)):
        x = lines[i]
        dataset[i] = lines[i].strip('\n')
        i += 1
    f.close()
     
    while True:
        x = random.randint(0, 19)
        ran = dataset[x]        
        hangman_game(ran)