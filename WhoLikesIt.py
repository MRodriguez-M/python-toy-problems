"""
Implement a function which must take in input array, containing the names of people who like an item.
It must return the display text as shown in the examples:

likes [] must be "no one likes this"
likes ["Peter"] must be "Peter likes this"
likes ["Jacob", "Alex"] must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in "and 2 others" simply increases.
"""

def likes(names):
    output = ""
    # If statement to execute if list has no names
    if len(names) == 0:
        output = "no one likes this"
    # Elif statement to execute if list has only 1 name
    elif len(names) == 1:
        output = names[0] + " likes this"
    elif len(names) == 3:
        for n in range(len(names)):
            output = output + likeList[n] + ", "
        output = output + "like this"
    return output

likeList = []
endPrompt = False

# While loop to keep prompting user for names to add to list
while endPrompt != True:
    # Prompt user for name
    userInput = input("Add name (enter q to finish): ")
    # If statement to check that user input is not "q"
    if userInput != "q":
        # Add name to list
        likeList.append(userInput)
        endPrompt = False
    else:
        # Change Boolean to end prompt if user input is "q"
        endPrompt = True
# Print output based list of names by calling function
print("\n" + likes(likeList))