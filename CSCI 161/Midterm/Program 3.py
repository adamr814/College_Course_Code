'''
Adam Roy
CSCI 161
MIDTERM Program 3
'''

def clamp(val):
    if val < 0:
        return 0
    elif val >= 0 and val <= 255:
        return val
    elif val > 255:
        return 255

def main():
    inp = int(input("Enter a number: "))
    f = clamp(inp)
    print(f)
main()
        