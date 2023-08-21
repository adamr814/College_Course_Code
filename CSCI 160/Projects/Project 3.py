'''
Adam Roy
Project 3
CSCi 160
'''

def main():
    open_file()
    menu()
    
def open_file():
    f = 'books.txt'
    f = open(f, 'w')
    return f

def menu(f):
    print('Menu')
    d = {}
    choice = str(input('1 - Add book\n2 - Print all books\n3 - Search for a book\n4 - Take an order\n5 - Search by price\n6 - Exit\n'))
    
    
    if choice == "1":
        add_book(d)
    elif choice == "2":
        print_all_books(d, f)
    elif choice == "3":
        search_for_book(d)
    elif choice == "4":
        take_order(d)
    elif choice == "5":
        search_by_price(d)
    elif choice == "6":
        exit(f)
    else:
        print('You must select an option')
        print('Try again')
        menu()
        
def add_book(d):
    key = input('Enter a book title: ')
    value = float(input('Enter a book price: '))
    d[(key)] = value
    
def print_all_books(d, f):
    for (key, value) in d.items():
        print(key, value)
        f.write('%s:%s\n' % (key, value))
    
def search_for_book(d):
    search = input('Enter a book title: ')
    for (key, value) in d.items():
        if search == key:
            print('Book found')
            print(key, value)
        else:
            print('No books found')
    
def take_order(d):
    cost = 0
    q = 0
    while order != '':
        book = input('Enter book: ')
        qu = int(input('Quantity: '))
        q += qu
        bQ = d.get(book)
        cost = cost + (bQ * qu)
    print()
    print('Book order: ')
    print('Total books:', q)
    print('Total cost:', cost)     
                    
def search_by_price(d):
    sbp = input('Enter a book price')
    for (key, value) in d.items():
        if sbp == value:
            print('Book found')
            print(key, value)
        else:
            print('No books found')
            
def exit(f):
    f.close(f)
    os._exit(0)
    
main()