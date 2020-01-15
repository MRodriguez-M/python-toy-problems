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

# Class to manage item name, price, quantity, and description
class ItemToPurchase:
    # initialize attributes for name, price, quantity, description
    def __init__(self, name= "none", price= 0, quantity= 0, description= "none"):
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity
        self.itemDescription = description
        
    # Class method to calculate and output item cost
    def printItemCost(self):
        print("%s %d @ $%d = $%d" % (self.itemName, self.itemQuantity, self.itemPrice, (self.itemQuantity * self.itemPrice)))

    # Class method to output item and its description
    def printItemDescription(self):
        print("%s: %s" % (self.itemName, self.itemDescription))

# Class to manage options related to shopping cart menu
class ShoppingCart:
    # Initialize attributes for customer name, date, and shopping cart
    def __init__(self, customer= "none", date= "January 1, 2016", cart= []):
        self.customerName = customer
        self.currentDate = date
        self.cartItems = cart

    # Class method to add an item to the cart
    def addItem(self, itemInfo):
        # Prompt user for item information
        name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = int(input("Enter the item price: "))
        quantity = int(input("Enter the item quantity: "))
        # Append all user input into cart list as a list
        self.cartItems.append(ItemToPurchase(name, price, quantity, description))

    def removeItem(self):
        pass

    def modifyItem(self):
        pass

    # Class method that uses a for loop to return total number of items in the cart
    def getNumItemsInCart(self):
        itemCount = 0
        for i in self.cartItems:
            itemCount += 1
        return itemCount

    # Class method that uses a for loop to calculate and return total cost of all items in the cart
    def getCostOfCart(self):
        cost = 0
        totalCost = 0
        for i in self.cartItems:
            cost = i.itemPrice * i.itemQuantity
            totalCost += cost
        return totalCost

    # Class method that outputs all cart information
    def printTotal(self):
        # Output user name and current date
        print("%s's Shopping Cart - %s" % (self.customerName, self.currentDate))
        # If-else statement to check if shoppping cart is empty
        if self.getCostOfCart() == 0:
            # Print error message if cart is empty
            print("SHOPPING CART IS EMPTY")
        else:
            # Call method to output number of items in cart
            print("Number of items:", self.getNumItemsInCart())
            print("")
            # Call method from ItemToPurchase class to output individual item information
            ItemToPurchase().printItemCost()
            # Call method to output total cost
            print("\nTotal: $%d" % self.getCostOfCart())
    
    # Class method that outputs all item descriptions
    def printDescriptions(self):
        print("%s's Shopping Cart - %s" % (self.customerName, self.currentDate))
        print("\nItem Descriptions")
        # Call method from ItemToPurchase class to output item descriptions
        ItemToPurchase().printItemDescription()

# Function to output menu options and prompt user to select an option
def printMenu():
    # Output menu
    print("\nMENU"
    "\na - Add item to cart"
    "\nr - Remove item from cart"
    "\nc - Change item quantity"
    "\ni - Output items' descriptions"
    "\no - Output shopping cart"
    "\nq - Quit\n")

    # Prompt user to select an option
    menuOption = input("Choose an option: ")

    # While loop to continue prompting if user input is not menu option
    while menuOption != "q" and menuOption != "a" and menuOption != "r" and menuOption != "c" and menuOption != "i" and menuOption != "o":
        menuOption = input("Choose an option: ")
    return menuOption

# Create instance for information that will be accessed from the ShoppingCart and ItemToPurchase classes
userInfo = ShoppingCart()
itemInfo = ItemToPurchase()
# Prompt user for name and date
userInfo.customerName = input("Enter customer's name: ")
userInfo.currentDate = input("Enter today's date: ")

# Output user name and current date
print("Customer name:", userInfo.customerName)
print("Today's date:", userInfo.currentDate)

# Create global variable and call printMenu function
selectedOption = printMenu()
# While loop to check that selected option is not "q", will exit program if it is
while selectedOption != "q":
    # If statement to execute if selected option is "a"
    if selectedOption == "a":
        print("\nADD ITEM TO CART")
        # Call class method to add item to cart
        userInfo.addItem(itemInfo)
        selectedOption = printMenu()
    # Elif statement to execute if selected option is "i"
    elif selectedOption == "i":
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        # Call class method to output all item descriptions
        userInfo.printDescriptions()
        selectedOption = printMenu()
    # Elif statement to execute if selected option is "o"
    elif selectedOption == "o":
        print("\nOUTPUT SHOPPING CART")
        # Call class method to output all shopping cart information
        userInfo.printTotal()
        selectedOption = printMenu()