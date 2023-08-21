'''
Adam Roy
CSCI 161
Assignment 8
'''
import math
import os
class ShoppingCart:
    #This class contains customer data, the date, and cart items
    def _init_(self):
        self.customer_name = "none"
        self.current_date = "none"
        self.cart_items = []
    def add_item(self):
        ci = ShoppingCart()
        
        items = []
        items.append("TEST")#input("Enter the item name: "))
        items.append("TEST") #input("Enter the item description: "))
        items.append(2.00) #input("Enter the item price: "))
        items.append(2) #input("Enter the item quantity: "))
        ci.cart_items.extend(items)
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
        option = 'none'
        print('''
        MENU
        a - Add item to cart.
        i - Output items' descriptions
        o - Output shopping cart
        q - Quit
        ''')
        option = "a" #input("Choose an option: ").lower
        return option
                   
def main():
    option = ShoppingCart()
    inputs = ShoppingCart()
    inputs.customer_name = "JD" #input("Enter the customer's name: ")
    inputs.current_date = "1/1/21" #input("Enter today's date: ")
    print("\nCustomer name:", inputs.customer_name)
    print("Today's date:", inputs.current_date)
    pMu = print_menu()
    while pMu != 'q':
        if pMu == 'q' or pMu == 'Q':
            print("Thank you, goodbye")
            os._exit(0)
        elif pMu == 'a':
            option.add_item()
        elif pMu == 'i':
            j = 0
            k = 1
            print(oid.customer_name, "'s Shopping Cart - ", oid.current_date, sep='')
            print("Item Descriptions")
            for i in range(0, (len(oid.cart_items) / 4)):
                print(oid.cart_items[j], oid.cart_items[k])
                j += 4
                k += 4
        elif pMu == 'o':
            print(osc.customer_name, "'s Shopping Cart - ", osc.current_date, sep='')
            print((len(osc.cart_items) // 4))
            total = 0
            j = 2
            a = 0
            b = 2
            c = 3
            for i in range(0, (len(osc.cart_items) / 4)):
                print(osc.cart_items[a], " ", osc.cart_items[b], "@ $", osc.cart_items[c], " = ", round(float(osc.cart_items[b]) * float(osc.cart_items[c]), 2), sep='')
                price = price + int(osc.cart_items[j])
                i += 1
                J += 4
                a += 4
                b += 4
                c += 4
            print("Total price = $", price, sep='') 
        else:
            pMu
main()
    
                       
        
        
        