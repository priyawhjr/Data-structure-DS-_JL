

#Practice 1: The "Contact Finder" (Linear Search)

#Task: Create a program that searches for 
# a specific name in a list of contacts.

#nput: Create a list contacts = ["Alice", "Bob", "Charlie", "David", "Eve"].

'''User Input: Ask the user "Who are you looking for?".
Logic (Linear) Hint (Give if needed):
Loop through the list from start to end.
If contacts[i] == user_input, print "Found [Name] at index [i]".
If the loop finishes without finding it, print "Contact not found".'''

# Predefined contact list
contacts = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Take user input
name = input("Who are you looking for? ")

found = False

# Linear Search
for i in range(len(contacts)):
    if contacts[i].lower() == name.lower():
        print(f"Found {contacts[i]} at index {i}")
        found = True
        break

if not found:
    print("Contact not found")
#=====================================

print('\n\nBinary Search : ')
names = list(map(str, input("please create a list of names ").split()))
key = input("which name are you looking for? ")

if key not in names:
    print("ERROR: NAME NOT FOUND")
else:
    for i in range(len(names)):
        if names[i] == key:
            print("Key exists at index: " + str(i))
            break
