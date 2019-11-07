"""
(1) Use a loop to output a right triangle of height triangle_height.
The first line will have one user-specified character, such as % or *.
Each subsequent line will have one additional user-specified character until the number in the triangle's base reaches triangle_height.
Output a space after each user-specified character, including a line's last user-specified character.

Enter a character: %
Enter triangle height: 5
% 
% % 
% % % 
% % % % 
% % % % % 
"""

# Prompt user for character and triangle height
triangle_char = input("Enter a character: ")
triangle_height = int(input("Enter triangle height: "))

# Create variable to print user character plus space
triangle_space = triangle_char + " "

# For loop to create the right triangle based on user input
for h in range(triangle_height):
    print(triangle_space * (h + 1))