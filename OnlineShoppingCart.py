"""
(1) Build the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()

Ex. of print_item_cost() output:

Bottled Water 10 @ $1 = $10

(2) In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

Item 1
Enter the item name: Chocolate Chips
Enter the item price: 3
Enter the item quantity: 1

Item 2
Enter the item name: Bottled Water
Enter the item price: 1
Enter the item quantity: 10

(3) Add the costs of the two items together and output the total cost.

TOTAL COST
Chocolate Chips 1 @ $3 = $3
Bottled Water 10 @ $1 = $10

Total: $13
"""

# Class to manage item name, price, and quantity
class ItemToPurchase:
    # initialize attributes for name, price, quantity
    def __init__(self, name= "none", price= 0, quantity= 0):
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity
        
    # Class method to calculate and output item cost
    def printItemCost(self):
        print("%s %d @ $%d = $%d" % (self.itemName, self.itemQuantity, self.itemPrice, (self.itemQuantity * self.itemPrice)))