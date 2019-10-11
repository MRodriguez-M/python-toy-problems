"""
(1) Prompt the user to input a food item name, price, and quantity.
Output an itemized receipt.

Enter food item name: hot dog
Enter item price: 2
Enter item quantity: 5

RECEIPT
5 hot dog @ $ 2.0 = $ 10.0
Total cost: $ 10.0

(2) Extend the program to prompt the user for a second item.
Output an itemized receipt.

Enter food item name: hot dog
Enter item price: 2
Enter item quantity: 5

RECEIPT
5 hot dog @ $ 2.0 = $ 10.0
Total cost: $ 10.0


Enter second food item name: ice cream
Enter item price: 2.50
Enter item quantity: 4

RECEIPT
5 hot dog @ $ 2.0 = $ 10.0
4 ice cream @ $ 2.5 = $ 10.0
Total cost: $ 20.0

(3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost.
Output the total cost, the cost of gratuity, and the grand total.

Enter food item name: hot dog
Enter item price: 2
Enter item quantity: 5

RECEIPT
5 hot dog @ $ 2.0 = $ 10.0
Total cost: $ 10.0


Enter second food item name: ice cream
Enter item price: 2.50
Enter item quantity: 4

RECEIPT
5 hot dog @ $ 2.0 = $ 10.0
4 ice cream @ $ 2.5 = $ 10.0
Total cost: $ 20.0

15% gratuity: $ 3.0
Total with tip: $ 23.0
"""

itemName = input("Enter food item name: ")
itemPrice = float(input("Enter item price: "))
itemQuantity = int(input("Enter item quantity: "))
itemTotal = itemQuantity * itemPrice

print("\nRECEIPT")
print(itemQuantity, itemName, "@ $", itemPrice, "= $", itemTotal)
print("Total cost: $", itemTotal)

itemName2 = input("\n\nEnter second food item name: ")
itemPrice2 = float(input("Enter item price: "))
itemQuantity2 = int(input("Enter item quantity: "))
itemTotal2 = itemQuantity2 * itemPrice2
totalCost = itemTotal + itemTotal2

print("\nRECEIPT")
print(itemQuantity, itemName, "@ $", itemPrice, "= $", itemTotal)
print(itemQuantity2, itemName2, "@ $", itemPrice2, "= $", itemTotal2)
print("Total cost: $", totalCost)