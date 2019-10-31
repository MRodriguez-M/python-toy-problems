"""
(1) Output a menu of automotive services and the corresponding cost of each service.

Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12

(2) Prompt the user for two services from the menu.

Select first service: Oil change

Select second service: Car wax

(3) Output an invoice for the services selected.
Output the cost for each service and the total cost.

Davy's auto shop invoice

Service 1: Oil change, $35
Service 2: Car wax, $12

Total: $47

(4) Extend the program to allow the user to enter a dash (-), which indicates no service.

Select first service: Tire rotation

Select second service: -


Davy's auto shop invoice

Service 1: Tire rotation, $19
Service 2: No service

Total: $19
"""

# Dictionary of available services
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

# Print list of available services
print("Davy's auto shop services"
      "\nOil change -- $35"
      "\nTire rotation -- $19"
      "\nCar wash -- $7"
      "\nCar wax -- $12")