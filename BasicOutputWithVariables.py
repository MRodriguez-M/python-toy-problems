"""
(1) Output the user's input.

Enter integer: 4
You entered: 4

(2) Extend to output the input squared and cubed.

Enter integer: 4
You entered: 4
4 squared is 16 
And 4 cubed is 64 !!

(3) Extend to get a second user input into userNum2. Output sum and product.

Enter integer: 4
You entered: 4
4 squared is 16 
And 4 cubed is 64 !!
Enter another integer: 5
4 + 5 is 9
4 * 5 is 20
"""

# Prompt user for a number
userNum = int(input("Enter integer: "))

# Output user input in three basic statements
print("You entered:", userNum)
print(userNum, "squared is", userNum * userNum)
print("And", userNum, "cubed is", userNum * userNum * userNum, "!!")

# Prompt user for a second number
userNum2 = int(input("Enter another integer: "))

# Output both user inputs using addition and multiplication
print(userNum, "+", userNum2, "is", userNum + userNum2)
print(userNum, "*", userNum2, "is", userNum * userNum2)