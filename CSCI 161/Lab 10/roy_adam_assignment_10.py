'''
Adam Roy
CSCI 161
Assignment 10
'''
#ver 1.2

import math
import os

class ShoppingCart:
    cart_items = []
    
    def _init_(self):
        self.customer_name = 'none'
        self.current_date = 'none'
        
    def add_item(self, obj):
        ItemToPurchase = []
        ItemToPurchase.append(input('\nEnter the item name: '))
        ItemToPurchase.append(input('Enter the item description: '))
        ItemToPurchase.append(input('Enter the item price: '))
        ItemToPurchase.append(input('Enter the item quantity: '))
        obj.cart_items.append(ItemToPurchase)
    
    def get_cost_of_cart(self, obj):
        i = 0
        total = 0
        for i in range(0, (len(obj.cart_items))):
            total = total + (float(obj.cart_items[i][2]) * int(obj.cart_items[i][3]))
            i += 1
        return total
        
    def print_total(self, obj):
        if len(obj.cart_items) != 0:
            print('Cart total is: $', obj.get_cost_of_cart(obj) , sep='')
        else:
            print('Shopping Cart Is Empty')
    
    def print_descriptions(self, obj):
        i = 0
        if len(obj.cart_items != 0):
            for i in range(0, (len(obj.cart_items))):
                print(obj.cart_items[i][0], ', ', obj.cart_items[i][1], sep='')
        else:
            print('Shoping Cart Is Empty')
    
    def remove_item(self, obj):
        i = 0
        remove = input('Enter a cart item to remove: ')
        for i in range(0, len(obj.cart_items)):
            if obj.cart_items[i][0] == remove:
                obj.cart_items[i].pop() 
            i += 1
        
    def modify_item(self, obj):
        i = 0
        change = input('Enter a cart item to adjust: ')
        for i in range(0, len(obj.cart_items)):
            if obj.cart_items[i][0] == change:
                val = int(input('Enter new quantity: '))
                obj.cart_items[i][3] = val
            i += 1
    
    def write_receipt_to_file(self, obj):
        file = input('Enter file name: ')
        f = open(file, 'w')
        i = 0
        f.write('---RECEIPT---\n\n')
        line = str(obj.customer_name) + '\'s Shopping Cart - ' + str(obj.current_date) + '\n'
        f.write(line)
        line = 'Number of Items:' + str(len(obj.cart_items)) + '\n'
        f.write(line)
        for i in range(0, len(obj.cart_items)):
            line = str(i + 1) + '.' + str(obj.cart_items[i][0]) + ' ' + str(obj.cart_items[i][3]) + ' @ $' + str(obj.cart_items[i][2]) + ' = $' + str(round(float(obj.cart_items[i][2]) * int(obj.cart_items[i][3]), 2)) + '\n'
            f.write(line)
            line = '-Item Description: ' + str(obj.cart_items[i][1]) + '\n'
            f.write(line)
            i += 1
        line = '\nCart total is: $' + str(obj.get_cost_of_cart(obj))    
        f.write(line)
        f.write('\n\n---RECEIPT---\n')
        f.close()
        
    def view_receipt_file(self, obj):
        file = input('Enter file name: ')
        receipt = open(file, 'r')
        lines = receipt.readlines()
        for line in lines:
            print(line)
        receipt.close
    
def main():
    obj = ShoppingCart()
    obj.customer_name = input('Enter the Customer\'s name: ')
    obj.current_date = input('\nEnter today\'s date: ')
    print('\n\nCustomer name:', obj.customer_name)
    print('\nToday\'s date:', obj.current_date)
    print_menu(obj)
        
def print_menu(obj):
    choice = 'none'
    print('''
MENU
    a - Add item to cart
    r - Remove item from the cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    f - Finalize order
    v - View receipt
    q - Quit''')
    choice = str(input('Choose an option: '))
    if choice.isalpha() == False:
        print('\nInvalid Character entered')
        print_menu(obj)
    else:
        while choice != 'q':
            if choice == 'o' or choice == 'O':
                i = 0
                print('\n', obj.customer_name, '\'s Shopping Cart - ', obj.current_date, sep='')
                print('\nNumber of Items:', (len(obj.cart_items)))
                for i in range(0, (len(obj.cart_items))):
                    print(obj.cart_items[i][0], ' ', obj.cart_items[i][3], ' @ $', obj.cart_items[i][2], ' = $', round(float(obj.cart_items[i][2]) * int(obj.cart_items[i][3]), 2), sep='')
                    i += 1
                obj.print_total(obj)
            elif choice == 'i' or choice == 'I':
                i = 0
                print('\n', obj.customer_name, '\'s Shopping Cart - ', obj.current_date, sep='')
                print('\nItem Descritions:')
                for i in range(0, (len(obj.cart_items))):
                    print(obj.cart_items[i][0], ', ', obj.cart_items[i][1], sep='')
                    i += 1
            elif choice == 'c' or choice == 'C':
                obj.modify_item(obj)
            elif choice == 'r' or choice == 'R':
                obj.remove_item(obj)
            elif choice == 'a' or choice == 'A':
                obj.add_item(obj)
            elif choice == 'f' or choice == 'F':
                obj.write_receipt_to_file(obj)
                ch = input('Are you sure you are done shopping? (y/n)\n')
                if ch == 'y':
                    os._exit(0)
                else:
                    continue
            elif choice == 'v' or choice == 'V':
                obj.view_receipt_file(obj)
                ch = input('Do you want to continue? (y/n)\n')
                if ch == 'n':
                    os._exit(0)
                else:
                    continue                
                
            else:
                print('\nInvaid input please try again\n')
            
            print('''
MENU
    a - Add item to cart
    r - Remove item from the cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    f - Finalize order
    v - View receipt
    q - Quit''')
            choice = str(input('Choose an option: '))            
main()
                    
                
            
        
    

    
    
                
            
        
    
    