"""
(1) Prompt the user to enter four numbers, each corresponding to a person's weight in pounds.
Store all weights in a list.
Output the list.

Enter weight 1: 236
Enter weight 2: 89.5
Enter weight 3: 176.0
Enter weight 4: 166.3

Weights: [236.0, 89.5, 176.0, 166.3]

(2) Output the average of the list's elements.

Enter weight 1: 236
Enter weight 2: 89.5
Enter weight 3: 176.0
Enter weight 4: 166.3

Weights: [236.0, 89.5, 176.0, 166.3]
Average weight: 166.95

(3) Output the max list element.

Enter weight 1: 236
Enter weight 2: 89.5
Enter weight 3: 176.0
Enter weight 4: 166.3

Weights: [236.0, 89.5, 176.0, 166.3]
Average weight: 166.95
Max weight: 236.0

(4) Prompt the user for a number between 1 and 4.
Output the weight at the user specified location and the corresponding value in kilograms.
1 kilogram is equal to 2.2 pounds.

Enter a list index (1 - 4): 3
Weight in pounds: 176.0
Weight in kilograms: 80.0

(5) Sort the list's elements from least heavy to heaviest weight.

Sorted list: [89.5, 166.3, 176.0, 236.0]
"""

# Prompt user for four weights
weight1 = float(input("Enter weight 1: "))
weight2 = float(input("Enter weight 2: "))
weight3 = float(input("Enter weight 3: "))
weight4 = float(input("Enter weight 4: "))

# Create list with four weights
weights = []
weights.append(weight1)
weights.append(weight2)
weights.append(weight3)
weights.append(weight4)

# Output list of weights
print("\nWeights:", weights)