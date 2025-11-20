## Session2 : Control Structures 

## while loop 
# print numbers from 0 to 4
n = 0
while n <5:
    print(n)
    n = n + 1
print('End')

# Be careful with infinite loops

# in this example, the condition is always true, 
# because x is never updated inside the loop (x = x + 1 is missing)
x = 0
while x < 5:
    print(x)

# break statement
# look for the first number divisible by 4 and 3
# when found, exit the loop
x = 0
while x < 20:
    if x % 4 == 0 and x % 3 == 0 :
        print(f'First number divisible by 4 and 3 is: {x}')
        break
    x += 1
  
# continue statement
# print numbers from 0 to 4, but skip 2
n = 0
while n < 4:      
    n += 1
    if n == 2:
        continue # if n is 2, skip the rest of the loop and go to the next iteration
    print(n)

# or:
n = 0
while n < 5:      
    if n == 2:
        n += 1
        continue # if n is 2, skip the rest of the loop and go to the next iteration
    print(n)
    n += 1

# simple ChatBoot
print("Hello, I'm yourChatbot!")
 
while True:
    user_query =input("What do you want:")
    if user_query =="" :
        continue
    if user_query =="END":
        break
    print("Okay, I will do:",user_query)
 
print("Bye!")

## for loop

# simple example:
for i in range(5):
    print(i)

# customized range:
for i in range(2,10,2):  # [2,4,6,8] 10 is excluded
    print(i)

# a mathematical sequence
# U = 1^2 + 2^2 + 3^2 + ... + 20^n
n = 20
U = 0

for k in range(1, n +1):
    U = U + k**2

print("U =", U)

# Lists:
names = ['Mohamed', 'Ali', 'Khalid']
# indexing:   0       1       2
# indexing:  -3      -2      -1

# List manipulation
print( names[0])
print( names[-1])  #last element

names[1] = 'Omar'  # modify element at index 1 to 'Omar'

print("Mohamed" in names)  # True
print("Said" in names)    # False

# read all names using
for name in names:
    # you cann't use the variable name to change the list element
    print(name) 

# Read and/or modify list elements using their indices
for i in range(len(names)):
    print( names[i])
    names[i] = "student" + names[i]  # modify each name by adding "student"


# add 4 points to each note that is equal to 10
notes = [10,12,15,13,10,15,20]

for i in range(len(notes)):
    if notes[i] == 10:
        notes[i] += 4 

print( notes)
