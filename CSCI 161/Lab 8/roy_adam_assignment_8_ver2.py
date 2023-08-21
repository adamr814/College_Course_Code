'''
Adam Roy
CSCI 161
Assignment 8

Could not figure out why this program would not run correctly
'''
import math
import os

class ShoppingCart:
    def _init_(self):
        self.customer_name = "none"
        self.current_date = "none"
        self.cart_items = []
    def add_item(self):
        item = []
        item.append(input("Enter the item name: "))
        item.append(input("Enter the item description: "))
        item.append(input("Enter the item price: "))
        item.append(input("Enter the item quantity: "))
        return item
    def get_cost_of_cart(self):
        price = 0
        j = 2
        for i in range(0, len(self.cart_items)):
            price = price + self.cart_items[j]
            j += 4
            i += 1
        return price
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(round(self.get_cost_of_cart))
    def print_descriptions(self):
        j = 0
        k = 1
        for i in range(0, len(self.cart_items)):
            print(self.cart_items[j], ', ', self.cart_items[k], sep='')
            j += 4
            k += 4
def print_menu():
    print('''
    MENU
    a - Add item to cart.
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    ''')
    option = str(input("Choose an option: "))
    return option
def main():
    inputs = ShoppingCart()
    inputs.customer_name = input("Enter the customer's name: ")
    inputs.current_date = input("Enter today's date: ")
    print("\nCustomer name:", inputs.customer_name)
    print("Today's date:", inputs.current_date)
    op = print_menu()
    while op != 'q':
        if op == 'q':
            print("Thank you, goodbye")
            os._exit(0)
        elif op == 'a':
            inputs.add_item
        elif op == 'i':
            j = 0
            k = 1
            print(inputs.customer_name, "'s Shopping Cart - ", inputs.current_date, sep='')
            print("Item Descriptions")
            for i in range(0, (len(inputs.cart_items) / 4)):
                print(inputs.cart_items[j], inputs.cart_items[k])
                j += 4
                k += 4
        elif op == 'o':
            print(inputs.customer_name, "'s Shopping Cart - ", inputs.current_date, sep='')
            print((len(inputs.cart_items) // 4))
            total = 0
            j = 2
            a = 0
            b = 2
            c = 3
            for i in range(0, (len(inputs.cart_items) / 4)):
                print(inputs.cart_items[a], " ", inputs.cart_items[b], "@ $", inputs.cart_items[c], " = ", round(float(osc.cart_items[b]) * float(osc.cart_items[c]), 2), sep='')
                price = price + int(inputs.cart_items[j])
                i += 1
                J += 4
                a += 4
                b += 4
                c += 4
            print("Total price = $", price, sep='')
        else:
            print("Invalid input, please enter a new value\n")
        op = print_menu()    
main()
            
    
