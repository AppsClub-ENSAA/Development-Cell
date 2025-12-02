## Session 4: Data Structures (List, Set, Dictionary, Tuple)

# 1. Dictionary

# Define a dictionary:
# Let's say we want to make a contact notebook
contacts = {
    "ahmed": "0641859476",
    "mohamed": "0671789412"
}

# Print the dictionary 
print(contacts)

# Access a value by its key
print(contacts["ahmed"])

# Check if a key exists in our dictionary
print("mohamed" in contacts)  # True
print("ali" in contacts)      # False

# Adding a new pair of key:value
contacts["ali"] = "0696784512"

# Iterate through a dictionary
for person in contacts:
    print("Tel number of", person, "is", contacts[person])

## Dictionary Methods:

# To get all keys
keys = contacts.keys()
# To get all values
values = contacts.values()
# To get all pairs (items)
items = contacts.items()

for person, tel in items:
    print("Tel number of", person, "is", tel)

# Safe access: to avoid getting an error when the key doesn't exist
tel = contacts.get("Khalid", "Not found") 
# If "Khalid" doesn't exist, it will return "Not found"

# Removing an item from the dictionary
contacts.pop("ali")

# Remove all items
contacts.clear()


# 2. Set

# Define a set:
ids = {"#1579", "#0791", "#79541"} # A set of IDs
# or ids = set() if there are no initial items

print(ids)

# Add a new item
ids.add("#154")
ids.update(["#1489", "#7220"])

# Removing items
ids.remove("#154")   # Raises Error if not found
ids.discard("#999")  # No Error if not found

# Clear the set
ids.clear()

## Operations on Sets
# Let's say we have two sets
S1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
S2 = {5, 6, 7, 8, 9, 10, 11, 12}

# Union (All elements from both)
S3 = S1.union(S2) # Result: {1, 2, ..., 12}
# OR: S3 = S1 | S2

# Intersection (Common elements)
S4 = S1.intersection(S2) # Result: {5, 6, 7, 8, 9}
# OR: S4 = S1 & S2

# Difference (In S1 but not in S2)
S5 = S1.difference(S2) # Result: {1, 2, 3, 4}
# OR: S5 = S1 - S2


# 3. Tuples

# Let's take an example of coordinates 
coordinates = (10, 5)  # (x, y)

# Standard print
print("My coordinates are: (", coordinates[0], ",", coordinates[1], ")")
# Or using f-string (Cleaner way)
print(f"My coordinates are: ({coordinates[0]}, {coordinates[1]})")

# Tuples are immutable (we can't change their content)
# coordinates[0] = 12  # Error!

# Tuple assignment (Unpacking)
x, y = coordinates
print(x) # x = 10
print(y) # y = 5

# Comparing two tuples (it compares element by element)
print((1, 2, 3) < (1, 7, 9)) # True

# Tuples as keys of dictionary
# Same example of contacts but with (first_name, last_name) as key

directory = {}  # Empty directory
person1 = ("ali", "alami")
person2 = ("mohamed", "khaldi")

directory[person1] = "0614784910"
directory[person2] = "0678941579"

tel = directory[("ali", "alami")] 
print(tel) # 0614784910

print(directory)
"""
Output:
{
    ('ali', 'alami'): '0614784910', 
    ('mohamed', 'khaldi'): '0678941579'
}
"""