## Session 5: 
## Part 1: Try and Except (Error Handling)
# if we try to make a simple division calculator we may many errors like division by zero or invalid input:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception :
    print("An unexpected error occurred.")

# Important: as you can see we go from specific error handling to a general one 
# Another example: 
# As we see in the previous session, we can use the get method to safely access dictionary values.
# Now let's see how to do it using try and except:
contacts = {
    "ahmed": "0641859476",
    "mohamed": "0671789412"
}
try:
    name = input("Enter the contact name  ")
    print("Tel of",name,"is",contacts[name])
except KeyError:
    print("Error: The contact "+name+" does not exist.") 

## Part 2: f-Strings and pass keyword
# f-Strings: A way to format strings easily insetad of using concatenation or the format method
name = "Ahmed"
age = 25

# Using concatenation
sentence1 = "My name is " + name + " and I am " + str(age) + " years old." 
# Using f-Strings syntax
sentence2 = f"My name is {name} and I am {age} years old."

# pass keyword: means "do nothing" , used meanly as a placeholder
# example of a function that we haven't implemented yet:
def future_function():
    pass  # To be implemented later

future_function()  # This will do nothing for now


# Part 3: OOP or Object Oriented Programming
# OOP a programming paradigm that organizes programs as "objects", which are 
# a combination of data (attributes) and the functions (methods) that operate on that data

# Class: A blueprint for creating objects or a template (like a factory)
# Object: An instance of a class (like a product made by the factory)

# Example:
class Human:
    pass

Ali = Human()  # Creating an object of the Human class
print(type(Ali))  # <class '__main__.Human'>
Fatima = Human()  # Another object of the Human class
print(type(Fatima))  # <class '__main__.Human'>

# Constructor: A special method used to initialize new objects 

# Example: lets say we hava a Car class with attributes brand, model, and year
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car("Toyota", "Corolla", 2020)

print(f"My car is a {my_car.brand} {my_car.model}.")
print("Year:", my_car.year)

# Methods: Functions defined inside a class that operate on the object's data
# Example: Adding a method to the Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.for_sale = False

    def display_info(self):
        print(f"Car Info: {self.brand} {self.model}, Year: {self.year}")

    def sell(self):
        self.for_sale = True
        print(f"My car {self.brand} {self.model} is now for sale.")

my_car = Car("Honda", "Civic", 2019)
# To display car information
my_car.display_info()
# If you want to sell the car
my_car.sell()