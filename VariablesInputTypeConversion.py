"""
(1) Prompt the user to input an integer between 0 and 155, a float, a character, and a string, storing each into separate variables.
Then, output those four values on a single line separated by a space.

Enter integer (0 - 155): 99
Enter float: 3.77
Enter character: z
Enter string: Howdy
99 3.77 z Howdy

(2) Extend to also output in reverse.

Enter integer (0 - 155): 99
Enter float: 3.77
Enter character: z
Enter string: Howdy
99 3.77 z Howdy
Howdy z 3.77 99

(3) Extend to convert the integer to a character by using the 'chr()' function, and output that character.

Enter integer (0 - 155): 99
Enter float: 3.77
Enter character: z
Enter string: Howdy
99 3.77 z Howdy
Howdy z 3.77 99
99 converted to a character is c
"""

userInt = int(input("Enter integer (0 - 155): "))
userFloat = float(input("Enter float: "))
userChar = (input("Enter character: "))
userStr = (input("Enter string: "))

print(userInt, userFloat, userChar, userStr)
print(userStr, userChar, userFloat, userInt)