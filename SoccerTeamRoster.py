"""
(1) Prompt the user to input five pairs of numbers: A player's jersey number (0 - 99) and the player's rating (1 - 9).
Store the jersey numbers and the ratings in a dictionary.
Output the dictionary's elements with the jersey numbers in ascending order (i.e., output the roster from smallest to largest jersey number).

Enter player 1's jersey number: 84
Enter player 1's rating: 7

Enter player 2's jersey number: 23
Enter player 2's rating: 4

Enter player 3's jersey number: 4
Enter player 3's rating: 5

Enter player 4's jersey number: 30
Enter player 4's rating: 2

Enter player 5's jersey number: 66
Enter player 5's rating: 9


ROSTER
Jersey number: 4, Rating: 5
Jersey number: 23, Rating: 4
Jersey number 30, Rating: 2
...

(2) Implement a menu of options for a user to modify the roster.
Each option is represented by a single character.
The program initially outputs the menu, and outputs the menu after a user chooses an option.
The program ends when the user chooses the option to Quit.
For this step, the other options do nothing.

MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit

Choose an option: 

(3) Implement the "Output roster" menu option.

ROSTER
Jersey number: 4, Rating: 5
Jersey number: 23, Rating: 4
Jersey number 30, Rating: 2
...

(4) Implement the "Add player" menu option.
Prompt the user for a new player's jersey number and rating.
Append the values to the two vectors.

Enter a new player's jersey number: 49
Enter the player's rating: 8

(5) Implement the "Delete player" menu option.
Prompt the user for a player's jersey number.
Remove the player from the roster (delete the jersey number and rating).

Enter a jersey number: 4

(6) Implement the "Update player rating" menu option.
Prompt the user for a player's jersey number.
Prompt again for a new rating for the player, and then change that player's rating.

Enter a jersey number: 23
Enter a new rating for player: 6

(7) Implement the "Output players above a rating" menu option.
Prompt the user for a rating.
Print the jersey number and rating for all players with ratings above the entered value.

Enter a rating: 5

ABOVE 5
Jersey number: 66, Rating: 9
Jersey number: 84, Rating: 7
...
"""

# Variables to help create dictionary of five players
count = 1
rosterDict = {}

# While Loop to get user input for information for five players
while count <= 5:
    jerseyNumber = int(input("Enter player %d's jersey number: " % count))
    rating = int(input("Enter player %d's rating: " % count))
    print("")
    # Add information into a dictionary
    rosterDict[jerseyNumber] = rating
    # Convert dictionary into a list
    rosterList = list(rosterDict.keys())
    count += 1

# Sort list based on jersey number
rosterList = sorted(rosterList)
print("\nROSTER")
# For loop to output player information
for jerseyNumber in rosterList:
    print("Jersey number: %d, Rating: %d" % (jerseyNumber, rosterDict[jerseyNumber]))

# Output menu options
menu = """
\nMENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
"""
print(menu)

# While loop to continue prompting until user input is "q"
while True:
    # Prompt user to select an option from the menu
    menuOption = input("Choose an option: ")
    
    # If statement to check that input is not "q"
    if menuOption != "q":
        # If statement to execute if user input is "o"
        if menuOption == "o":
            print("\nROSTER")
            # For loop to output player information
            for jerseyNumber in rosterList:
                print("Jersey number: %d, Rating: %d" % (jerseyNumber, rosterDict[jerseyNumber]))
            print(menu)
        # Elif statement to execute if user input is "a"
        elif menuOption == "a":
            # Create variable to help add new player to dictionary
            newRosterDict = {}
            # Prompt user for new player jersey number and rating
            addJerseyNumber = int(input("\nEnter a new player's jersey number: "))
            addRating = int(input("Enter the player's rating: "))
            # Add new information into a dictionary
            newRosterDict[addJerseyNumber] = addRating
            # Add dictionary with new information to dictionary with existing player information
            rosterDict.update(newRosterDict)
            # Convert dictionary into a list
            rosterList = list(rosterDict.keys())
            # Sort list based on jersey number
            rosterList = sorted(rosterList)
            print(menu)
        # Elif statment to execute if user input is "d"
        elif menuOption == "d":
            # Prompt user for jersey number to remove from roster
            deletePlayer = int(input("\nEnter a jersey number: "))
            # Delete player information from dictionary
            del rosterDict[deletePlayer]
            # Convert updated dictionary into a list
            rosterList = list(rosterDict.keys())
            # Sort list based on jersey number
            rosterList = sorted(rosterList)
            print(menu)
        # Elif statement to execute if user input is "u"
        elif menuOption == "u":
            # Create variable to help add updated player information to dictionary
            updateRosterDict = {}
            # Prompt user for player jersey number and new rating
            updateJerseyNumber = int(input("\nEnter a jersey number: "))
            updateRating = int(input("Enter a new rating for player: "))
            # Add updated information into a dictionary
            updateRosterDict[updateJerseyNumber] = updateRating
            # Add dictionary with updated information to dictionary with existing player information
            rosterDict.update(updateRosterDict)
            # Convert dictionary into a list
            rosterList = list(rosterDict.keys())
            # Sort list based on jersey number
            rosterList = sorted(rosterList)
            print(menu)
        # Elif statement to execute to if user input is "r"
        elif menuOption == "r":
            # Prompt user for rating
            aboveRating = int(input("\nEnter a rating: "))
            print("\nABOVE", aboveRating)
            # For loop to check dictionary for ratings above user input
            for j, r in rosterDict.items():
                # Output player information if rating is above user input
                if r > aboveRating:
                    print("Jersey number: %d, Rating: %d" % (j, r))
                else:
                    # Do not print and continue to loop through dictionary if rating is not above user input
                    continue
            print(menu)
    else:
        # Break to exit program if user input is "q"
        break