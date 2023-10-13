import re

# Read in the search term from the user
search_term = input("Enter the search term: ")

# Replace any underscores in the search term with a regex pattern that matches any character
search_regex = search_term.replace("_", ".")

# Open the file and search for the search term
with open("passwords.txt", "r", encoding="utf-8") as f:
    for line in f:
        if re.search(search_regex, line):
            print(line.strip())

# Prompt the user to press enter to exit the program
input("Press enter to exit...")
