"""
(1) Prompt the user for an automobile service.
Output the user's input.

Enter desired auto service: Oil change
You entered: Oil change

(2) Output the price of the requested service.

Cost of oil change: $35

The program should support the following services:
Oil change -- $35
Tire rotation -- $19
Car wash -- $7

If the user enters a service that is not listed above, then output the following error message:
Error: Requested service is not recognized.
"""
# Dictionary for available services
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7
}

# Prompt user for service desired and output user input
autoService = input("Enter desired service: ")
print("You entered:", autoService)

if autoService in services:
    print("\nCost of", autoService.lower() + ": $%s" % services[autoService])