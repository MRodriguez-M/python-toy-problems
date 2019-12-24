"""
(1) Prompt the user to enter a string of their choosing.
Store the text in a string.
Output the string.

Enter a sample text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

(2) Implement a menu function, which has a string as a parameter, outputs a menu of user options for analyzing/editing the string, and returns the user's entered menu option and the sample text string (which can be edited inside the menu function).
Each option is represented by a single character. 
If an invalid character is entered, continue to prompt for a valid choice.

MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

Choose an option: 

(3) Implement the number of non-whitespace characters function.
Number of non-whitespace characters function has a string parameter and returns the number of characters in the string, excluding all whitespace.
Call number of non-whitespace characters function in the menu function.

Number of non-whitespace characters: 181

(4) Implement the number of words function.
Number of words function has a string parameter and returns the number of words in the string.
Call number of words function in the menu function.

Number of words: 35

(5) Implement the fix capitalization function.
Fix capitalization function has a string parameter and returns an updated string, where lowercase letters at the beginning of sentences are replaced with uppercase letters.
Fix capitalization function also returns the number of letters that have been capitalized.
Call fix capitalization function in the menu function, and then output the number of letters capitalized and the edited string.

Number of letters capitalized: 3
Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!


(6) Implement the replace punctuation function.
Replace punctuation function has a string parameter and two keyword argument parameters exclamationCount and semicolonCount.
Replace punctuation function updates the string by replacing each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,).
Replace punctuation function also counts the number of times each character is replaced and outputs those counts.
Lastly, replace punctuation function returns the updated string.
Call replace punctuation function in the menu function, and then output the edited string.

Punctuation replaced
exclamationCount: 1
semicolonCount: 2
Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.

(7) Implement the shorten spaces function.
Shorten spaces function has a string parameter and updates the string by replacing all sequences of 2 or more spaces with a single space.
Shorten spaces function returns the string.
Call shorten spaces function in the menu function, and then output the edited string.

Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes, more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!
"""

# Function to output menu options and prompt user to select an option
def menu(userString):
    # Output menu
    print("\nMENU"
    "\nc - Number of non-whitespace characters"
    "\nw - Number of words"
    "\nf - Fix capitalization"
    "\nr - Replace punctuation"
    "\ns - Shorten spaces"
    "\nq - Quit\n")

    # Prompt user to select an option
    menuOption = input("Choose an option: ")

    # While loop to continue prompting if user input is not menu option
    while menuOption != "q" and menuOption != "c" and menuOption != "w": #FIXME add other menu options
        menuOption = input("Choose an option: ")
    return menuOption

# Function to output number of non-whitespace characters in user string
def nonWhitespaceChar(userString):
    # Remove whitespace
    newUserString = userString.replace(" ", "").replace("\t", "")
    count = 0
    # For loop to count number of characters in non-whitespace string
    for i in range(len(newUserString)):
        count += 1
    return count

# Function to output the number of words in user string
def numWords(userString):
    # Split() combined with len() counts number of words in string based on whitespace
    words = len(userString.split())
    return words

# Prompt user for string and output user input
userString = input("Enter a sample text: ")
print("\nYou entered:", userString)

# Create global variable and call menu function
selectedOption = menu(userString)
# While loop to check that selected menu option is not "q", will exit program if it is
while selectedOption != "q":
    # If statement to execute if selected menu option is "c"
    if selectedOption == "c":
        # Call non-whitespace characters function
        print("\nNumber of non-whitespace characters:", nonWhitespaceChar(userString))
        selectedOption = menu(userString)
    # Elif statement to execute if selected menu option is "w"
    elif selectedOption == "w":
        # Call number of words function
        print("\nNumber of words:", numWords(userString))
        selectedOption = menu(userString)