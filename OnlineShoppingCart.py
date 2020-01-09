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

(4) Extend the ItemToPurchase class to contain a new attribute.
item_description (string) - Set to "none" in default constructor 
Implement the following method for the ItemToPurchase class.
print_item_description() - Has an ItemToPurchase parameter

Ex. of print_item_description() output:

Bottled Water: Deer Park, 12 oz.

(5) Build the ShoppingCart class with the following data attributes and related methods.
Parameterized constructor which takes the customer name and date as parameters

Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2016"
cart_items (list)

Methods
add_item()
Adds an item to cart_items list.
Has parameter ItemToPurchase.
Does not return anything.
remove_item()
Removes item from cart_items list.
Has a string (an item's name) parameter.
Does not return anything.
If item name cannot be found, output this message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's description, price, and/or quantity.
Has parameter ItemToPurchase.
Does not return anything.
If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity.
If not, modify item in cart.
If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
get_num_items_in_cart()
Returns quantity of all items in cart.
Has no parameters.
get_cost_of_cart()
Determines and returns the total cost of items in cart.
Has no parameters. 
print_total()
Outputs total of objects in cart.
If cart is empty, output this message: SHOPPING CART IS EMPTY
print_descriptions()
Outputs each item's description. 

Ex. of print_total() output:

John Doe's Shopping Cart - February 1, 2016
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521

Ex. of print_descriptions() output:

John Doe's Shopping Cart - February 1, 2016

Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones


(6) In main section of your code, prompt the user for a customer's name and today's date.
Output the name and date.
Create an object of type ShoppingCart.

Enter customer's name: John Doe
Enter today's date: February 1, 2016
Customer name: John Doe
Today's date: February 1, 2016

(7) Implement the print_menu() function. print_menu() has a ShoppingCart parameter, and outputs a menu of options to manipulate the shopping cart.
Each option is represented by a single character.
Build and output the menu within the function.
If the an invalid character is entered, continue to prompt for a valid choice.
Call print_menu() in the main() function.
Continue to execute the menu until the user enters q to Quit.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option: 

(8) Implement Output shopping cart menu option.

OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2016
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521

(9) Implement Output item's description menu option.

OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2016

Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

(10) Implement Add item to cart menu option.

ADD ITEM TO CART
Enter the item name: Nike Romaleos
Enter the item description: Volt color, Weightlifting shoes
Enter the item price: 189
Enter the item quantity: 2

(11) Implement remove item menu option.

REMOVE ITEM FROM CART
Enter name of item to remove: Chocolate Chips

(12) Implement Change item quantity menu option.

CHANGE ITEM QUANTITY
Enter the item name: Nike Romaleos
Enter the new quantity: 3
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

# Create instance for item 1
item1 = ItemToPurchase()
print("Item 1")
# Prompt user for name, price, and quantity of item 1
item1.itemName = input("Enter the item name: ")
item1.itemPrice = int(input("Enter the item price: "))
item1.itemQuantity = int(input("Enter the item quantity: "))

# Create instance for item 2
item2 = ItemToPurchase()
print("\nItem 2")
# Prompt user for name, price, and quantity of item 2
item2.itemName = input("Enter the item name: ")
item2.itemPrice = int(input("Enter the item price: "))
item2.itemQuantity = int(input("Enter the item quantity: "))

# Calculate total cost of items 1 and 2
totalCost = (item1.itemPrice * item1.itemQuantity) + (item2.itemPrice * item2.itemQuantity)
print("\nTOTAL COST")
# Output costs information for item 1 and item 2
item1.printItemCost()
item2.printItemCost()
# Output total cost for both items
print("\nTotal: $%d" % totalCost)