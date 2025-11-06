## Variables and Data Types
# assigning different types of values to variables
Club = "AppsClub"
is_my_favorite_club = True
members = 1000
price = 10.00

# Printing Variables
print("my favorite club is " , Club)
print("it has " , members , " members")

# Variables data types
print(type(Club))                    # str
print(type(is_my_favorite_club))     # bool
print(type(members))                 # int
print(type(price))                   # float

# Data Type Manipulation
a = 15
b = 6
c = a + b 
print(a / b)
print(a // b)
print(a % b)
c = c + 1
print(c ** 3)

# String Manipulation
f_name = "ahmed"
l_name = "karim"
full_name = f_name + "" + l_name
line ="-"
print(line * 20)

# Boolean Logic
a = 10
b = 5
compare = (a == b)
compare = (a >= b)
compare = a != b and a > 7
compare = a < b or b > 0

# variable casting
num = "10"
num = int(num)
print(type(num))

word = "10L"
word = float(word)  # This will raise an error

num  = 15
num = str(num)
print(type(num))

# Input Handling
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the club.")

# Python Tricks
x, y = 5, 10

x, y = y, x

a = b = c = 0

### Control Flow Statements
## Conditional Statements

# Example 1:
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Example 2:
temp = float(input("Enter the temperature: "))

if temp < 15:
    print("It's a cold day!")
elif temp < 30:
    print("Nice weather today!")
else:
    print("It's a hot day!")

