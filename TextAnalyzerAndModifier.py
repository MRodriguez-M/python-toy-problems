"""
(1) Prompt the user to enter a string of their choosing.
Output the string.

Enter a sentence or phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.

(2) Complete a function which returns the number of characters in the user's string.

(3) Calling the function and output the returned result.

Enter a sentence or phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.

Number of characters: 46

(4) Extend the program further by implementing a function that outputs the string's characters except for whitespace.

Enter a sentence or phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.

Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.
"""

# Function to count number of characters in user input
def numOfCharacters():
    count = 0
    for i in range(len(userString)):
        count += 1
    return count

# Prompting user for string and printing user input
userString = input("Enter a sentence or phrase: ")
print("You entered:", userString)

# Output number of characters in user input
print("\nNumber of characters:", numOfCharacters())