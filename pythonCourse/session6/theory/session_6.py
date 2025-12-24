## Session 6:
## Part 1: Instance vs Class Attributes
print("="*100)
"""
A good example to illustrate the difference between the two kinds of attributes is to consider a student at the university.
Let's the university assigns each student a unique ID number when they enroll.  
So the very first student will get ID number 1, the second student will get ID number 2, and so on.
As you may notice, to keep track of the ID numbers, we need a variable that is shared among all students (objects) 
to know what the next ID number should be, and this variable should belong to the class itself, not to any specific student.

In the example below: name and id are instance attributes because they are specific to each student object.
But next_id is a class attribute because it is shared among all instances of the Student class.
"""
class Student:
    next_id = 1  

    def __init__(self, name):
        self.name = name  
        self.id = Student.next_id  # Assign the current next_id to the student's id
        Student.next_id += 1  # Increment the class attribute for the next student

ali = Student("Ali")
mohamed = Student("Mohamed")
print(ali.name, ali.id)        # Output: Ali 1
print(mohamed.name, mohamed.id)  # Output: Mohamed 2

## Part 2: Methods (Instance and Static Methods)
print("="*100)
"""
Simply we can say a static method is a method that belongs to the class rather than any specific instance of the class.
So it can be called on the class itself, without needing to create an instance of the class.
In the example below, we can use the MathHelper class to perform mathematical operations without creating an object of the class.
"""
class MathHelper:
    @staticmethod
    def is_even( number):
        return number % 2 == 0
    
    @staticmethod
    def sum( *args):  # args is a tuple of all the arguments passed to the method: sum( 1,2,3,4 ) => args = (1,2,3,4)
        S = 0
        for n in args:
            S += n
        return S

print( MathHelper.is_even(4) ) # True
S = MathHelper.sum(1,2,3,4)  # 10   
print( S)

## Part 3: Inheritance
print("="*100)
"""
Inheritance is a fundamental concept in OOP that allows a class (called the child or subclass) to inherit 
attributes and methods from another class (called the parent or superclass).
"""
class Person:
    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def present_yourself(self):
        print(f"Hi, I am {self.first_name} and I have {self.age} years old.")

class Student( Person):
    def __init__(self, f_name, l_name, age, shcool_class, homework):
        # we pass the common attributes to the parent class constructor
        super().__init__(f_name, l_name, age)

        # we set the specific attributes for the Student class
        self.school_class = shcool_class
        self.homework = homework

    def get_homework(self):
        print( f'my homework:{ self.homework}')

student_ali = Student("Ali", "Ahmed", 20, "CS101", "Math exercises")
student_ali.present_yourself()  # Inherited method from Person class
student_ali.get_homework()  # Specific method from Student class

## Part 4: Encapsulation
print("="*100)
"""
Encapsulation is alsoone of the fundamental principles of OOP.
It refers to the bundling of data (attributes) and methods (functions) that operate on that data within a single unit or class.
Which restreicts direct access to an object's data and methods from outside the class.

In the example below, we have a BankAccount class with a private attribute __balance (we don't someone to access it from outside the class).
we can also define a private method that is only used internally within the class, in our case the __add_fee method is used to calculate 
the total amount to withdraw including a fee.
"""
class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.__balance = 0
    
    # we check first amount before depositing
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount   

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= self.__add_fee(amount)

    def __add_fee(self, amount):
        return amount + 5  # Deduct a fee of 5 DH

    def get_balance(self):
        return self.__balance
    
account = BankAccount("Ali")
account.deposit(100)
account.withdraw(50)   # 50 + 5 fee = 55 will be deducted

# print(account.__balance)  # This will raise an AttributeError
print( account.get_balance() )  # This will print the current balance: 45

## Part 5: Abstraction
print("="*100)
"""
Another fundamental principle of OOP is Abstraction.
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object.
This allows as to interact just with a contracted interface, without needing to understand the inner workings of the object.

In our example both Car and Boat classes implement the abstract class Vehicule (The Contract)
So whatever I use a Car or a Boat, I know that both have the move and stop methods.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass    

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving on road")

    def stop(self):
        print("Car stopped")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water")

    def stop(self):
        print("Boat anchored")
    
## Part 6: Polymorphism
"""
The last fundamental principle of OOP is Polymorphism.
It allows the same method, function, or operator to behave differently depending on the object.
There is 3 levels of polymorphism:
1. Method Overriding: When a subclass overrides (changes) the behavior of a method inherited from its parent class.
2. Methos Overloading: When multiple methods in the same class have the same name but different parameters (not directly supported in Python).
3. Operator Overloading: When we define custom behavior for operators (like +, -, *, etc.) for our own classes.
"""

# Method Overriding example: here each subclass provides its own implementation of the sound method (overriding the parent class method)
class Animal:
    def sound(self):
        return "Somesound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
    
animals =[Dog(), Cat(), Animal()]

for a in animals:
    print(a.sound()) # Bark,Meow, Somesound

# Method Overloading example: the behavior of the say_hi method changes based on the number of arguments passed to it
class Welcome:
    @staticmethod
    def say_hi(name="Mr. X"):
        print(f"Hello {name}")

Welcome.say_hi() # Output: Hello Mr. X
Welcome.say_hi("Ahmed") # Output: Hello Ahmed


# Operator Overloading example:
"""
we already know that the + operator is used to add two numbers ,or concatenate two strings, ...
but we can overload the + operator to work with our own classes.
Note: we can also override other operators like -, *, /, etc by defining special methods in our class (google it).
"""

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2  
print(v3)  # Output: Vector(6, 8)


## End of session 6
## End of Python Course
## Thank you !!!