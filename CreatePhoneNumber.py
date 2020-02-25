"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] returns "(123) 456-7890"
"""

# Function to create phone number in proper format
def createPhoneNumber():
    # Create variable for formatted phone number
    phoneNumber = "("
    # For loop to add first three digits to phone number
    for digit in numberList[:3]:
        phoneNumber = phoneNumber + digit
    
    phoneNumber = phoneNumber + ") "
    # For lopp to add next three digits to phone number
    for digit in numberList[3:6]:
        phoneNumber = phoneNumber + digit

    phoneNumber = phoneNumber + "-"
    # For loop to add last four digits to phone number
    for digit in numberList[6:]:
        phoneNumber = phoneNumber + digit
    return phoneNumber

# Prompt user for 10 digits that will make up phone number
userDigits = input("Enter 10-digit phone number (digits only): ")

# If statement to check that user input is only digits
if userDigits.isdigit():
    # If statment to check that user input is only 10 digits
    if len(userDigits) == 10:
        # Change user input into list and call function
        numberList = list(userDigits)
        print(createPhoneNumber())
    else:
        # Print error message if user input is not exactly 10 digits
        print("Error: Number needs to be 10 digits.")
else:
    # Print error message if user input has characters other than digits
    print("Error: Number must be digits only.")