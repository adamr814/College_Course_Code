'''
Adam Roy
FINAL PROGRAM Part 5
CSCI 161
'''
#ver 1.5
import os

pizzas = {'Margarita': 5, 'Hawaiian': 7, '4cheese': 6, 'Vegetarian': 6.5, 'Pepperoni': 9}
toppings = {'mushroom':1, 'onions': 2, 'green pepper':3, 'extra cheese':4}

def start():
    choice = input('Welcome! Would you like to order? (y/n): ')
    return choice

def pizza_choice(pizzas, toppings):
    print('Available Pizzas:\n')
    print('Margarita, Hawaiian, 4cheese, Vegetarian, Pepperoni\n')
    pC = input('Please choose a pizza: ')
    if (pC in pizzas) == True:
        print('Selected pizza:', pC)
    else:
        print('We currently do not have that pizza')
        pizza_choice(pizzas, toppings)
    print('Available Toppings\n')
    print('mushroom, onions, green pepper, extra cheese\n')    
    tC = input('Please choose a topping: ')
    if (tC in toppings) == True:
        print('Selected toppings:', tC)
    else:
        print('We currently do not have those toppings')
        pizza_choice(pizzas, toppings)
    print('Final order:', pC, 'with', tC)
    choice = input('Would you like to change your order? (y/n): ')
    if choice == 'y' or choice == 'Y':
        pizza_choice(pizzas, toppings)
    else:
        pT = pizzas.get(pC)
        tT = toppings.get(tC)
        total = (pT + tT)
        print('Your total is $', total, sep='')
        

    
    
def main():
    choice = start()
    if choice == 'y' or choice == 'Y':
        print('Hi, welcome to our text based pizza ordering')
        pizza_choice(pizzas, toppings)
main()
    