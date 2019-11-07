"""
This program outputs a downwards facing arrow composed of a rectangle and a right triangle.
The arrow dimensions are defined by user specified arrow base height, arrow base width, and arrow head width.

(1) Use a loop to output an arrow base of height arrow_base_height.

(2) Use a loop to output an arrow base of width arrow_base_width.

(3) Use a loop to output an arrow head of width arrow_head_width.

(4) Allow program to only accept an arrow head width that is larger than the arrow base width.
Use a loop to continue prompting the user for an arrow head width until the value is larger than the arrow base width.

Enter arrow base height: 5
Enter arrow base width: 2
Enter arrow head width: 4
**
**
**
**
**
****
***
**
*
"""

# Prompt user for dimensions of half arrow
arrow_base_height = int(input("Enter arrow base height: "))
arrow_base_width = int(input("Enter arrow base width: "))
arrow_head_width = int(input("Enter arrow head width: "))

# For loop to print rectangle part of half arrow
for h in range(arrow_base_height):
    h = "*" * arrow_base_width
    print(h)