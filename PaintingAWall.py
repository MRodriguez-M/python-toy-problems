"""
(1) Prompt the user to input a wall's height and width.
Calculate and output the wall's area.

Enter wall height (feet): 12
Enter wall width (feet): 15
Wall area: 180.0 square feet

(2) Extend to also calculate and output the amount of paint in gallons needed to paint the wall.
Assume a gallon of paint covers 350 square feet.
Store this value in a variable.

Enter wall height (feet): 12
Enter wall width (feet): 15
Wall area: 180.0 square feet
Paint needed: 0.5142857142857142 gallons

(3) Extend to also calculate and output the number of 1 gallon cans needed to paint the wall.

Enter wall height (feet): 12
Enter wall width (feet): 15
Wall area: 180.0 square feet
Paint needed: 0.5142857142857142 gallons
Cans needed: 1 can(s)

(4) Extend by prompting the user for a color they want to paint the walls.
Calculate and output the total cost of the paint cans depending on which color is chosen.
Use a dictionary to associate each paint color with its respective cost. 
Red paint costs $35 per gallon can, blue paint costs $25 per gallon can, and green paint costs $23 per gallon can.

Enter wall height (feet): 12
Enter wall width (feet): 15
Wall area: 180.0 square feet
Paint needed: 0.5142857142857142 gallons
Cans needed: 1 can(s)

Choose a color to paint the wall: red
Cost of purchasing red paint: $35
"""
import math

# Prompt user for wall height and width
wallHeight = float(input("Enter wall height (feet): "))
wallWidth = float(input("Enter wall width (feet): "))

# Calculate and output area of wall
wallArea = wallHeight * wallWidth
print("Wall area:", wallArea, "square feet")

# Calculate and output amount of paint needed
paintNeeded = wallArea / 350
print("Paint needed:", paintNeeded, "gallons")

# Calculate and output number of cans of paint needed
cansNeeded = math.ceil(paintNeeded)
print("Cans needed:", cansNeeded, "can(s)")