"""
(1) Prompt the user for a title for data. Output the title.

Enter a title for the data: Number of Novels Authored
You entered: Number of Novels Authored

(2) Prompt the user for the headers of two columns of a table.
Output the column headers.

Enter the column 1 header: Author name
You entered: Author name

Enter the column 2 header: Number of novels
You entered: Number of novels

(3) Prompt the user for data points.
Data points must be in this format: string, int.
Store the information before the comma into a string variable and the information after the comma into an integer.
The user will enter -1 when they have finished entering data points.
Output the data points.
Store the string components of the data points in a list of strings.
Store the integer components of the data points in a list of integers.

Enter a data point (-1 to stop input): Jane Austen, 6
Data string: Jane Austen
Data integer: 6

(4) Perform error checking for the data point entries.
If any of the following errors occurs, output the appropriate error message and prompt again for a valid data point.
If entry has no comma
Output: Error: No comma in string.
If entry has more than one comma
Output: Error: Too many commas in input.
If entry after the comma is not an integer
Output: Error: Comma not followed by an integer.

Enter a data point (-1 to stop input): Ernest Hemingway 9
Error: No comma in string.

Enter a data point (-1 to stop input): Ernest, Hemingway, 9
Error: Too many commas in input.

Enter a data point (-1 to stop input): Ernest Hemingway, nine
Error: Comma not followed by an integer.

Enter a valid data point: Ernest Hemingway, 9
Data string: Ernest Hemingway
Data integer: 9

(5) Output the information in a formatted table.
The title is right justified with a minimum field width value of 33.
Column 1 has a minimum field width value of 20.
Column 2 has a minimum field width value of 23.

        Number of Novels Authored
Author name         |       Number of novels
--------------------------------------------
Jane Austen         |                      6
Charles Dickens     |                     20
Ernest Hemingway    |                      9
Jack Kerouac        |                     22
F. Scott Fitzgerald |                      8
Mary Shelley        |                      7
Charlotte Bronte    |                      5
Mark Twain          |                     11
Agatha Christie     |                     73
Ian Flemming        |                     14
J.K. Rowling        |                     14
Stephen King        |                     54
Oscar Wilde         |                      1

(6) Output the information as a formatted histogram.
Each name is right justified with a minimum field width value of 20.

         Jane Austen ******
     Charles Dickens ********************
    Ernest Hemingway *********
        Jack Kerouac **********************
 F. Scott Fitzgerald ********
        Mary Shelley *******
    Charlotte Bronte *****
          Mark Twain ***********
     Agatha Christie *************************************************************************
        Ian Flemming **************
        J.K. Rowling **************
        Stephen King ******************************************************
         Oscar Wilde *
"""

# Prompt user for data title and output user input
dataTitle = input("Enter a title for the data: ")
print("You entered:", dataTitle)

# Prompt user for column 1 header and output user input
column1 = input("\nEnter the column 1 header: ")
print("You entered:", column1)

# Prompt user for column 2 header and output user input
column2 = input("\nEnter the column 2 header: ")
print("You entered:", column2)

# Set variable for message to prompt user input
inputMessage = "\nEnter a data point (-1 to stop input): "
# Create list that will contain all data points
dataList = []

# While loop to continue prompting for data until user input is "-1"
while True:
    # Prompt user for data point
    dataPoint = input(inputMessage)

    # If statement to check that user input is not "-1"
    if dataPoint != "-1":
        # If statement to check for comma in user input
        if "," in dataPoint:
            # Use split method to split data point in two
            dataInfo = dataPoint.split(",")
            # If statement to check and output error message if user input has more than one comma and reassign message to prompt valid user input
            if len(dataInfo) > 2:
                print("Error: Too many commas in input.")
                inputMessage = "\nEnter a valid data point: "
            # Elif to check and output error message if second part of string is not an integer and reassign message to prompt valid user input
            elif not dataInfo[1].replace(" ", "").isdigit():
                print("Error: Comma not followed by an integer.")
                inputMessage = "\nEnter a valid data point: "
            else:
                # Output string and integer data separtely
                print("Data string:", dataInfo[0])
                print("Data integer:", dataInfo[1].replace(" ", ""))
                # Assign prompt message to original in case it was reassigned by an error message
                inputMessage = "\nEnter a data point (-1 to stop input): "
                # Add data points to end of list
                dataList.extend(dataInfo)
        # Output error message if no comma in user input and reassign message to prompt valid user input
        elif "," not in dataPoint:
            print("Error: No comma in string.")
            inputMessage = "\nEnter a valid data point: "
    else:
        # Break to stop prompting for data if user input is "-1"
        break

# Output title, both column titles, and a separting line of dashes for head of table
print("\n%33s" % dataTitle)
print("%-20s|%23s" % (column1, column2))
print("-" * 44)

# Create variable to iterate through dataList
index = 0
# While loop to print all elements in dataList to table
while index < len(dataList):
    print("%-20s|%23s" % (dataList[index], dataList[index + 1]))
    index += 2

# Create variable to iterate through dataList for histogram
i = 0
print("")
# While loop to print all elements in dataList to histogram
while i < len(dataList):
    print("%s %s" % (dataList[i], (int(dataList[i + 1]) * "*")))
    i += 2