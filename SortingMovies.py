"""
(1) Build a dictionary that contains the movie collection below.

Year          Title                       Director

2005          Munich                      Steven Spielberg
2006          The Prestige                Christopher Nolan
2006          The Departed                Martin Scorsese
2007          Into the Wild               Sean Penn
2008          The Dark Knight             Christopher Nolan
2009          Mary and Max                Adam Elliot
2010          The King's Speech           Tom Hooper
2011          The Artist                  Michel Hazanavicius
2011          The Help                    Tate Taylor
2012          Argo                        Ben Affleck
2013          12 Years a Slave            Steve McQueen
2014          Birdman                     Alejandro G. Inarritu
2015          Spotlight                   Tom McCarthy
2016          The BFG                     Steven Spielberg

(2) Prompt the user for a single year and output the movie title(s) and director(s) from that year.
Output N/A if the year is invalid.

Enter a year between 2005 and 2016:
2011
The Artist, Michel Hazanavicius
The Help, Tate Taylor

(3) After prompting the user for a year and displaying the title(s) and directors(s) from that year, display a menu.
The menu enables a user to display the movies sorted by year, director, or movie title.
Each option is represented by a single character.
The program initially outputs the menu, and outputs the menu after a user chooses an option.
If an invalid character is entered, continue to prompt for a valid choice.
The program ends when the user chooses the option to Quit.
For this step, the other options do nothing.

Enter a year between 2005 and 2016:
2011
The Artist, Michel Hazanavicius
The Help, Tate Taylor

MENU
Sort by:
y - Year
d - Director
t - Movie title
q - Quit

Choose an option:

(4) Implement the sort by year menu option.
Note: There is a newline and a tab between the year and the movie title/director.

...
Choose an option:
y
2005:
    Munich, Steven Spielberg

2006:
    The Prestige, Christopher Nolan
    The Departed, Martin Scorsese

2007:
    Into the Wild, Sean Penn

2008:
    The Dark Knight, Christopher Nolan

...

(5) Implement the sort by director menu option.
For directors with multiple films on the list, order their films by year.
Note: There is a newline and a tab between the director's name and the movie title/year.

...
Choose an option:
d
Adam Elliot:
    Mary and Max, 2009

Alejandro G. Inarritu:
    Birdman, 2014

Ben Affleck:
    Argo, 2012

Christopher Nolan:
    The Dark Knight, 2008
    The Prestige, 2006

...

(6) Implement the sort by movie title menu option.
Note: There is a newline and a tab between the movie title and the movie director/year.

...
Choose an option:
t
12 Years a Slave:
    Steve McQueen, 2013

Argo:
    Ben Affleck, 2012

Birdman:
    Alejandro G. Inarritu, 2014

Into the Wild:
    Sean Penn, 2007

...
"""

# Create dictionary with film year, title, and director
movieCollection = {
    "2005": [["Munich", "Steven Spielberg"]],
    "2006": [["The Prestige", "Christopher Nolan"], ["The Departed", "Martin Scorsese"]],
    "2007": [["Into the Wild", "Sean Penn"]],
    "2008": [["The Dark Knight", "Christopher Nolan"]],
    "2009": [["Mary and Max", "Adam Elliot"]],
    "2010": [["The King's Speech", "Tom Hooper"]],
    "2011": [["The Artist", "Michel Hazanavicius"], ["The Help", "Tate Taylor"]],
    "2012": [["Argo", "Ben Affleck"]],
    "2013": [["12 Years a Slave", "Steve McQueen"]],
    "2014": [["Birdman", "Alejandro G. Inarritu"]],
    "2015": [["Spotlight", "Tom McCarthy"]],
    "2016": [["The BFG", "Steven Spielberg"]]
}

# Prompt user for a year
year = input("Enter a year between 2005 and 2016:\n")

# If statement to check if user input is available in dictionary
if year in movieCollection:
    # Print film title and director based on user input
    for m in movieCollection.get(year):
        print(m[0] + ", " + m[1])
else:
    # Print error message if user input not in dictionary
    print("N/A")

# Create and output menu options
menu = """
MENU
Sort by:
y - Year
d - Director
t - Movie title
q - Quit
"""
print(menu)

# While loop to continue prompting until user input is "q"
while True:
    # Prompt user to select an option from the menu
    menuOption = input("Choose an option:\n")

    # If statement to check that user input is not "q"
    if menuOption != "q":
        # If statement to execute if user input is "y"
        if menuOption == "y":
            # For loop to output film year
            for y, film in movieCollection.items():
                print("%s:" % y)
                # For loop to output film title and director
                for title, director in film:
                    print("\t%s, %s" % (title, director))
                print("")
            print(menu)
        # Elif statement to execute if user input is "d"
        elif menuOption == "d":
            # Create variable to create new dictionary
            directorDict = {}
            # For loops to check for years, titles, and directors in dictionary
            for year, film in movieCollection.items():
                for title, director in film:
                    # If statement to check and add director not already key in new dictionary
                    if director not in directorDict:
                        directorDict[director] = []
                    # Add film title and year to corresponding director
                    directorDict[director].append([title, year])
            # For loop to output director name in alphabetical order based on first name
            for d, film in sorted(directorDict.items()):
                print("%s:" % d)
                # For loop to output film title and year
                for title, year in film:
                    print("\t%s, %s" % (title, year))
                print("")
            print(menu)
        # Elif statement to execute if user input is "t"
        elif menuOption == "t":
            # Create variable to create new dictionary
            titleDict = {}
            # For loops to check for years, titles, and directors in dictionary
            for year, film in movieCollection.items():
                for title, director in film:
                    # If statement to check and add title not already key in new dictionary
                    if title not in titleDict:
                        titleDict[title] = []
                    # Add film director and year to title
                    titleDict[title].append([director, year])
            # For loop to output film titles in alphabetical order
            for t, film in sorted(titleDict.items()):
                print("%s:" % t)
                # For loop to output film director and year
                for director, year in film:
                    print("\t%s, %s" % (director, year))
                print("")
            print(menu)
    else:
        # Break to exit program if user input is "q"
        break