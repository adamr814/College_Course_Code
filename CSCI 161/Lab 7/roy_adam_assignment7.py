'''
Adam Roy
Assignment 7
CSCI 161
'''
import math
class ItemToPurchase:
    #Contains item initilizations and print functions
    def _init_(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0
        
    def print_item_cost(self, item1, item2):
        print()
        costI1 = (item1.item_price * item1.item_quantity)
        print(item1.item_name, ", ", item1.item_quantity, " @ ", item1.item_price, " = $", round(costI1, 2), sep='')
        costI2 = (item2.item_price * item2.item_quantity)
        print(item2.item_name, ", ", item2.item_quantity, " @ ", item2.item_price, " = $", round(costI2, 2), sep='')
        print("\nTotal Cost: $", (costI1 + costI2), sep='')
        
    def item_description(self, item1, item2):
        print()
        print("Item Descriptions: ")
        print(item1.item_name, ": ", item1.item_description, sep='')
        print(item2.item_name, ": ", item2.item_description, sep='')
        
        
def main():
    print("Enter data for item 1:")
    item1 = ItemToPurchase()
    item1.item_name = input("Please enter the item name for item: ")
    item1.item_description = input("Please enter the item description: ")
    item1.item_price = float(input("Please enter the item price: "))
    item1.item_quantity= int(input("Please enter the quantity: "))
    print("\nEnter data for item 2:")
    item2 = ItemToPurchase()
    item2.item_name = input("Please enter the item name for item: ")
    item2.item_description = input("Please enter the item description: ")
    item2.item_price = float(input("Please enter the item price: "))
    item2.item_quantity= int(input("Please enter the quantity: "))
    
    TotalCost = ItemToPurchase()
    TotalCost.print_item_cost(item1, item2)
    Descriptions = ItemToPurchase()
    Descriptions.item_description(item1, item2)
    
main() 
        
