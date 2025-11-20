## Lists (continued from session_2)
# List Methods

notes = [ 10, 12, 15, 20]

notes.sort()            # notes =[10,12,15,20]

notes.append(18)        # notes =[10,12,15,20,18]
notes.insert(1, 13)     # notes =[10,13,12,15,20,18]
notes.extend([10,15])   # notes =[10,13,12,15,20,18,10,15]

notes.remove(10)        # notes =[13,12,15,20,18,10,15] (removes first occurrence of 10)
notes.pop(0)            # notes =[12,15,20,18,10,15] (removes element at index 0)
notes.pop()             # notes =[12,15,20,18,10] (removes last element)

notes.count(20)         # returns 1 (number of occurrences of 20)

# Slicing a list
sublist = notes[1:4:1]    # sublist = [15,20,18] (from index 1 to 3 (index 4 is out), step = 1)
sublist2 = notes[:3]      # sublist2 = [12,15,20] (from start to index 2)
sublist3 = notes[2:]      # sublist3 = [20,18,10] (from index 2 to end)
sublist4 = notes[::-1]    # sublist4 = [10,18,20,15,12] (reversed list, step = -1)

## Session 3: 
# Strings
fruit = "banana"

first_letter = fruit[0]   # 'b'
last_letter = fruit[-1]   # 'a'

print( 'b' in fruit)    # True

for char in fruit:
    print(char)         # prints each character in the string

sliced_fruit = fruit[1:4]   # 'ana' (from index 1 to 3)
reversed_fruit = fruit[::-1] # 'ananab' (reversed string)

# Strring are immutable
# fruit[0] = 'B'   # This will raise an error
# instead, we can create a new string :
new_fruit = 'B' + fruit[1:]  # 'Banana'

# Strings Methods:
Club = "AppsClub"

index = Club.find('C')        # 4 (index of first occurrence of 'C')
index2 = Club.find('z')       # -1 (not found)

upper_club = Club.upper()      # 'APPSCLUB'
lower_club = Club.lower()      # 'appsclub'

replaced_club = Club.replace('Apps', 'Code')  # 'CodeClub'

url = "www.appsclub.com/courses/python/session3"

categories = url.split('/')   # ['www.appsclub.com', 'courses', 'python', 'session3']

full_name = ["Mohmed", "Ali", "Ahmed"]
name = " ".join(full_name)   # "Mohmed Ali Ahmed"

## Functions in Python

# Built-in functions:predefined by Python
print("Hello, World!")
length = len("Python")   # 6
maximum = max([10, 20, 5])   # 20 

# Defining your own functions

def say_hello( name):
    print("Hello,", name)

say_hello("Mohamed")   # Hello, Mohamed
say_hello("Ali")      # Hello, Ali

# default value for name is "X"
def say_hello2( name="X"):   
    print("Hello,", name)

say_hello2()            # Hello, X
say_hello2("Khalid")    # Hello, Khalid

# functions with return values
def add_numbers( a, b):
    return a + b

S = add_numbers( 10, 20)
print("S =", S)
