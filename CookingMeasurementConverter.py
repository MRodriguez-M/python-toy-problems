"""
(1) Prompt the user for the number of cups of lemon juice, water, and sugar needed to make lemonade.
Prompt the user to specify the number of servings the recipe yields.
Output the ingredients and serving size.

Enter amount of lemon juice (in cups): 2
Enter amount of water (in cups): 16
Enter amount of agave nectar (in cups): 2.5
How many servings does this make? 6

Lemonade ingredients - yields 6.0 servings
2.0 cup(s) lemon juice
16.0 cup(s) water
2.5 cup(s) agave nectar

(2) Prompt the user to specify the desired number of servings.
Adjust the amounts of each ingredient accordingly, and then output the ingredients and serving size.

How many servings would you like to make?
48

Lemonade ingredients - yields 48.0 servings
16.0 cup(s) lemon juice
128.0 cup(s) water
20.0 cup(s) agave nectar

(3) Convert the ingredient measurements from (2) to gallons.
Output the ingredients and serving size. Note: There are 16 cups in a gallon.

Lemonade ingredients - yields 48.0 servings
1.0 gallon(s) lemon juice
8.0 gallon(s) water
1.25 gallon(s) agave nectar
"""

# Prompt user for ingredient amounts and serving size for recipe
lemonJuiceCups = float(input("Enter amount of lemon juice (in cups): "))
waterCups = float(input("Enter amount of water (in cups): "))
agaveNectarCups = float(input("Enter amount of agave nectar (in cups): "))
servingSize = float(input("How many servings does this make? "))

# Output recipe ingredients and serving size
print("\nLemonade ingredients - yields", servingSize, "servings")
print(lemonJuiceCups, "cup(s) lemon juice")
print(waterCups, "cup(s) water")
print(agaveNectarCups, "cup(s) agave nectar")

# Prompt user for amount of servings wanted
makeLemonade = float(input("\nHow many servings would you like to make? "))

# Calculate new ingredient amounts based on servings requested
newLemonJuice = ((makeLemonade / servingSize) * lemonJuiceCups)
newWater = ((makeLemonade / servingSize) * waterCups)
newAgaveNectar = ((makeLemonade / servingSize) * agaveNectarCups)

# Output ingredient amounts and servings based on user input
print("\nLemonade ingredients - yields", makeLemonade, "servings")
print(newLemonJuice, "cup(s) lemon juice")
print(newWater, "cup(s) water")
print(newAgaveNectar, "cup(s) agave nectar")

# Convert ingredient amounts from cups to gallons
gallonLemonJuice = (newLemonJuice / 16)
gallonWater = (newWater / 16)
gallonAgaveNectar = (newAgaveNectar / 16)

# Output ingredient amounts based on user requested servings in gallons
print("\nLemonade ingredients - yields", makeLemonade, "servings")
print(gallonLemonJuice, "gallon(s) lemon juice")
print(gallonWater, "gallon(s) water")
print(gallonAgaveNectar, "gallon(s) agave nectar")