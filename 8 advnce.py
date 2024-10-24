
# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Get user input for the search term
search_name = input("Enter a name to search for: ")

# Check if the name is in the list
if search_name in names:
    print("{search_name} is on the list.")
else:
    print("{search_name} is not on the list.")

