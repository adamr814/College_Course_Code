#Adam Roy
#CSCI 365
#Assignment 2 Question 2 Python

Input1 = list("/* this is a comment */")
Input2 = list("// this is a comment //")
Input3 = list("// this is a comment */")
Input4 = list("/* this is a comment /*")
Input5 = list("*/ this is a comment */")
Input6 = list("*/ this is a comment */")
Input7 = list("/* this is a */ comment */")

def ParseComment(Input):
    if Input[0] == "/" and Input[1] == "*" and Input[len(Input)-2] == "*" and Input[len(Input)-1] == "/":
        for i in range(2, (len(Input)-2)):
            if Input[i] == "*":
                return "Invalid Comment"
            else:
                next
        return "Valid Comment"
    else:
        return "Invalid Comment"

def main():
    pc1 = ParseComment(Input1)
    pc2 = ParseComment(Input2)
    pc3 = ParseComment(Input3)
    pc4 = ParseComment(Input4)
    pc5 = ParseComment(Input5)
    pc6 = ParseComment(Input6)
    pc7 = ParseComment(Input7)

    print("", pc1, "\n", pc2, "\n", pc3, "\n", pc4, "\n", pc5, "\n", pc6, "\n", pc7)
main()