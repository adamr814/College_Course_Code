#Adam Roy
#CSCI 365
#HW2 Q4 Python Program

#Variable declaration
charClass = 0
lexeme = 'a'
nextChar = 'a'
lexLen = 0
token = 0
nextToken = 0
charPos = 0
EOF = None
LET = 0
NUM = 1
UNK = 99

#Token Table
identifier = "<id>"
assign_op = "<assign_op>"
add_op = "<add_op>"
sub_op = "<sub_op>"
mult_op = "<mult_op>"
div_op = "<div_op>"
lparen = "<lparen>"
rparen = "<rparen>"
for_code = "<for>"
if_code = "<if>"
else_code = "<else>"
while_code = "<while>"
int_code = "<int>"
float_code = "<float>"
error_token = "<error>"
EOF = "<EOF>"

#Input File
inputFile = open("Q4.txt","r")
txtdata = inputFile.read()
N = len(txtdata)
def main():
    if (inputFile == None):
        print("Error Opening File\n")
    else:
        getChar()
        while nextToken != EOF:
            lex()
    inputFile.close()
    return 0
     
#Symbol Lookup
def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = lparen
    elif ch == ')':
        addChar()
        nextToken = rparen
    elif ch == '+':
        addChar()
        nextToken = add_op
    elif ch == '-':
        addChar()
        nextToken = sub_op
    elif ch == '*':
        addChar()
        nextToken = mult_op
    elif ch == '/':
        addChar()
        nextToken = div_op
    elif ch == '=':
        addChar()
        nextToken = assign_op
    else :
        addChar()
        nextToken = error_token
    return nextToken
   
#Adds Char To Lexeme
def addChar():
    global lexeme
    if lexLen <= 98:
        if lexeme == ' ':
            lexeme = nextChar
        else:
            lexeme = lexeme + nextChar
    else:
        print("Error - lexeme is too long \n")


#Gets Next Char
def getChar():
    global charPos
    global nextChar
    global charClass
    
    if N > charPos:
        nextChar = txtdata[charPos]
        charPos = charPos + 1
    else :
        nextChar = EOF
        charPos = charPos + 1
        
    if nextChar != EOF:
        if nextChar.isalpha():
            charClass = LET
        elif nextChar.isdigit():
            charClass = NUM
        else:
            charClass = UNK
    else:
        charClass = EOF

#Handling Blank Spaces
def getNonBlank():
    if nextChar != EOF:
        while nextChar.isspace():
            getChar()
    else:
        next

#Main Lexeme
def lex() :
    global lexeme
    global charClass
    global nextToken
    lexeme = ' '
    lexLen = 0
    getNonBlank()
    #Handling Chars
    if charClass == LET:
        addChar()
        getChar()
        while ((charClass == LET) or (charClass == NUM)):
            addChar()
            getChar()
        if lexeme == 'for':
            nextToken = for_code
        elif lexeme == 'if':
            nextToken = if_code
        elif lexeme == 'else':
            nextToken = else_code
        elif lexeme == 'while': 
            nextToken = while_code
        elif lexeme == 'int': 
            nextToken = int_code
        elif lexeme == 'float': 
            nextToken = float_code
        else:
            nextToken = identifier
    
    #Handling Nums
    elif charClass == NUM:
        addChar()
        getChar()
        while (charClass == NUM):
            addChar()
            getChar()
        nextToken = int_code

    #Handling Unknowns
    elif charClass == UNK:
       lookup(nextChar)
       getChar()

    #Handleing EOF
    elif charClass == EOF:
        nextToken = EOF
        lexeme = 'EOF'
    print("%11s,   %6s" %(nextToken, lexeme))
    return nextToken
main()