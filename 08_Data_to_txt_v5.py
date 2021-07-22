# Source: https://www.quru99.com/reading-and-writing-files-in-python.html

# Need to import the regular expression library re
import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a Filename (leave off the extension): ")

    # Regular expression to check file name. Can be Upper or lower case letters,
    valid_char = "[A-Za-z0-9_]"  # numberes or underscores
    for letter in filename:
        if re.match(valid_char, letter):
            continue  # If the letter is valid, goes back and checks the next

        elif letter == " ":  # otherwise, find problem
            problem = "(spaces not allowed)"

        else:
            problem = ("({}'s not allowed)".format(letter))
        has_error = "yes"
        break

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":  # describe problem
        print("Invalid filename - {}".format(problem))
        print()
    else:
        print("You entered a valid filename") # or allow a valid file name

# add .txt suffix!
filename = filename + ".txt"

# Create file to hold data
f = open(filename, "w+")

# add new line at the end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
