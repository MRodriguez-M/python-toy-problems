"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
    # Use lower() to make all characters lowercase so string is case insensitive
    stringList = s.lower()
    exList = []
    ohList = []
    # For loop to check each character in the string
    for i in stringList:
        # If statement to add character in string to list if it is "x"
        if i == "x":
            exList.append(i)
        # Elif statement to add character in string to list if it is "o"
        elif i == "o":
            ohList.append(i)