
# Exercise: Student Management System (OOP)

## Objective
In this exercise, we will build a small program to manage a classroom.

You will learn:
- How to create Classes (Blueprints).
- How to make Objects interact with each other.
- How to use Dictionaries to prevent duplicate data using unique IDs.

---

## Part 1: The Blueprints

### 1. The Student Class
Create a class that represents a person. It should just hold data.

Attributes:
- name
- id_number

Methods:
- __init__ only.

---

### 2. The Course Class
Create a class that represents the classroom manager.

Attributes:
- course_name
- gradebook (Empty Dictionary).

Methods:
- enroll_student(self, student_obj)
- give_grade(self, student_obj, grade)
- show_results(self)
- show_class_average(self)

---

## Part 2: The Logic (Key Concepts)

### The Gradebook Structure
We will not use a List. We will use a Dictionary.

Why?
Because looking up a student by their ID is faster and safer than looking them up by name.

The structure will look like this:

```python
self.gradebook = {
    "ID-101": {"name": "Amine", "grade": 15},
    "ID-102": {"name": "Sara", "grade": 18}
}
```

---

### Implementing enroll_student
Check if the student.id_number is already in the dictionary.  
If not, add them with a default grade of None.

---

### Implementing show_class_average
Create a variable total = 0.  
Create a variable count = 0.  
Loop through the gradebook.

Important: Check if grade is not None before adding to the total.

---

## Part 3: Testing Scenario

Copy and paste this code at the bottom of your file to test if your classes work correctly.

```python
# 1. Create 3 students
# Notice that s1 and s3 have the SAME NAME, but different IDs.
s1 = Student("Amine", "S-101")
s2 = Student("Sara",  "S-102")
s3 = Student("Amine", "S-103") 

# 2. Create the Course
my_course = Course("Python Basics")

# 3. Enroll everyone
my_course.enroll_student(s1)
my_course.enroll_student(s2)
my_course.enroll_student(s3)

# 4. Assign grades
# Because we use IDs internally, the program knows WHICH Amine is which.
my_course.give_grade(s1, 15)
my_course.give_grade(s2, 19)
my_course.give_grade(s3, 11)

# 5. Display
my_course.show_results()
my_course.show_class_average()
```

---

## Expected Output

If your logic is correct, you should see both Amines with their specific grades:

```
Amine: 15/20
Sara: 19/20
Amine: 11/20
--------------------
Class Average: 15.00/20
```
