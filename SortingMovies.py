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