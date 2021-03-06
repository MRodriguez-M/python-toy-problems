"""
(1) Prompt the user to enter two words and a number, storing each into separate variables.
Then, output those three values on a single line separated by a space.

Enter favorite color:
yellow                                                                                                                                                         
Enter pet's name:
Daisy                                                                                                                                                
Enter a number:
6

yellow Daisy 6

(2) Output two passwords using a combination of the user input.
Format the passwords as shown below.

Enter favorite color:
yellow                                                                                                                                                         
Enter pet's name:
Daisy                                                                                                                                                
Enter a number:
6

yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

(3) Output the length of each password (the number of characters in the strings).

Enter favorite color:
yellow                                                                                                                                                         
Enter pet's name:
Daisy                                                                                                                                                
Enter a number:
6

yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8
"""

# Prompt user for elements of password
favoriteColor = input("Enter favorite color:\n")
petName = input("Enter pet's name:\n")
number = input("Enter a number:\n")

# Output user input
print("\n" + favoriteColor, petName, number)

# Create templates for both passwords based on user input
password1 = favoriteColor + "_" + petName
password2 = number + favoriteColor + number

# Output both passwords using templates created
print("\nFirst password: %s_%s" % (favoriteColor, petName))
print("Second password: %s%s%s" % (number, favoriteColor, number))

# Output number of characters in each password generated
print("\nNumber of characters in", password1 + ": %d" % len(password1))
print("Number of characters in", password2 + ": %d" % len(password2))