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

# Prompt user for string and output user input
userString = input("Enter a sample text: ")
print("\nYou entered:", userString)