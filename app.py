# used for single line comments
''' this is a multi - line comment '''

'''number1 = 10
number2 = 15

sum = number1 + number2

print("The sum is:", sum)
#print("The product is:", product) this is commented because it has an error in it.

#variables. a variable is a container to holder data
number = 10 #number is a variable that stores 10
print("The number is:", number)

#use = to assign a value to a variable. The variable name is on the left and the value is on the right.
name = "John" #name is a variable that stores the string "John"
print(name)

#changing the value of a variable. You can change the value of a variable by assigning a new value to it.
name = "Jane" #name is now a variable that stores the string "Jane"
print(name)'''

#Literals - representations of a fixed value in a program.
#used to assign values to variables
#python type conversion - process of converting data of one type to another
'''Implicit type conversion - automatic conversion of data from one type to another
converting from integer to float 
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print("Value:",new_number)
print("Data Type:",type(new_number))'''

#explicit type conversion - manual conversion of data from one type to another by a user
#use built in functions to convert data types (int(), float(), str())
'''num_string = "123"
num_integer = 12
print("Data Type:",type(num_string))
#explicit conversion
num_string = int(num_string)
print("Data Type:",type(num_string))

num_sum = num_string + num_integer
print("The sum is:", num_sum)'''

#operand - value  that the oprator works on. In the example above, num_string and num_integer are operands and + is the operator.
# ** left operand raised to the power of right operand
# // floor division - returns the largest integer less than or equal to the result of the division
'''x = 15
y = 4
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)
print('x ** y = ',x**y)
#comparison operators return a boolean value (True or False) based on the comparison of two values.
print('x > y = ',x>y)
print('x < y = ',x<y)
print('x == y = ',x==y)
print('x != y = ',x!=y)'''

#logic operators - used to combine conditional statements
'''a = True
b = False
print('a and b = ',a and b)
print('a or b = ',a or b)
print('not a = ',not a)'''

#bitwise operators - used to perform bit level operations on binary numbers
'''x = 5 # binary: 0101
y = 3 # binary: 0011
print('x & y = ',x & y) # binary: 0001, decimal: 1 bitwise and
print('x | y = ',x | y) # binary: 0111, decimal: 7 bitwise or
print('x ^ y = ',x ^ y) # binary: 0110, decimal: 6 bitwise xor
print('~x = ',~x) # binary: 1010, decimal: -6 bitwise not
print('x << 1 = ',x << 1) # binary: 1010, decimal: 10 left shift
print('x >> 1 = ',x >> 1)''' # binary: 0010, decimal: 2 right shift

#identity operators, is and is not - They are used to check if two values (or variables) are located on the same part of the memory. 
'''x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)'''

#membership oprators, in and not in - used to test if a value or variable is found in a sequence (string, list, tuple, set and dictionary).
'''x4 = 'Hello world'
y4 = {1:'a', 2:'b'}
print('H' in x4)
print('hello' not in x4)'''

#if allows us to skip a block of code based on a specified condition

# Check if age is 18 or more
'''if age >= 18:
    print("Grant access to the website.")

print("Program complete.")'''

#if else allows us to execute a block of code between two alternatives
'''age = int(input("Enter your age: "))

if age >= 18:
    print("Grant access.")
else:
    print("Deny access.")'''
    
#authenticate user using if else
'''username_db = "Rinah"
password_db = "12345"
username = input("Enter your username: ")
password = input("Enter your password: ")
if (username == username_db and password == password_db):
    print("Grant access.")
else:
    print ("Deny access.")'''

#elif allows us to check multiple conditions
'''age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Grant access.")
else:
    print("Deny access.")'''

#largest of three numbers using if else and elif
# Taking input from the user
'''n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

print("The largest number is:", largest)'''

#for loop
#iterating through a list
'''fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("Program complete.")
#range() function - generates a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#iterating through a range of numbers
for i in range(1, 20, 2): #start, stop, step
    print(i)'''
    
#iterating through a string
'''language = "Python"
for x in language:
    print (x)'''

#for loop with else
'''stock = ['Laptop', 'Keyboard', 'Mouse']
order = input("Enter the product you want to buy: ")
for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")'''
       
#nested for loop
'''attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']
for attribute in attributes:
    # Inner loop
    for car in cars:
        print(attribute, car)
    
    print("-----")'''
    
#while loop is used to run a specified block of code until a specified condition is true
#infinite while looop
'''number = float(input("Enter a number: "))
while number >= 0:
    print(number)
    # Take number input again to solve the infinite loop situation
    number = float(input("Enter another number: "))'''
    
#while loop with else
'''attempts = 3
while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1212":
        print("Access granted.")
        break

    attempts -= 1
    print(f"Wrong PIN. {attempts} tries left.")
else:
    print("Account locked. Too many failed attempts.")'''
    
#continue statement is used to skip the current iteration of a loop and move to the next iteration.
'''for i in range(1, 11):

    # Condition to check if a number is even
    if i % 2 != 0:
        continue    #In the program, the loop iterates from i = 1 to 10. The if condition, i % 2 == 0, is True when i is even. In this case, the print() statement is skipped and the loop continues with the next iteration. That's why only odd numbers are printed.
    print(i)'''
    
#sum of only positive numbers 
'''total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))

    # Skip negative numbers
    if number < 0:
        continue

    # End the loop if the user enters 0
    if number == 0:
        break

    total += number

print(f"Sum of positive numbers: {total}")'''

#pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
'''is_valid = True

if is_valid:
    pass #if not put, it would bring invalid indentation error.
else:
    print("Login invalid. Redirect to form.")'''
    
#random module
'''import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())'''

#a function is a block of code that performs a specific task
'''def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')'''
  
#arguments are inputs given to a function
'''def greet(name):
    print('Hello', name)

# call the function
greet("Rinah")'''

'''def add_numbers(num1, num2):
    sum = num1 + num2
    print(sum)
add_numbers(1, 2)'''

#return statement used to return a value from a function
#code after return is not executed
'''def find_square(num):
    result = num * num
    return result
    result = num

# function call
square = find_square(3)

print('Square:', square)'''

#python library function
'''import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)'''

#function argument with default vales
'''def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)

# function call with two arguments
add_numbers(2, 3)  #returns 5

#  function call with one argument
add_numbers(a = 2) #returns 10 that is (2+8)

# function call with no arguments
add_numbers() #returns 15 that is (7+8)'''

# variable scope specifies the region where we can access a variable.
# local variables are declared inside a function and cant be accessed outside the function
'''def greet():
    message = "hello" #message is local to greet function
    print (message)
greet()
print(message) #brings an error'''

#global variable is declared outside a function
'''message = 'Hello' # declare global variable

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)'''

#the nonlocal keyword is used within nested functions to indicate that a variable is not local to the inner function, but rather belongs to an enclosing function’s scope. 
# outside function 
'''def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()'''

#global keyword is used to modify a global variable inside a function
'''a = 1
def add():
    global a
    a +=1
    print(a)
add()'''

#a recursion function is a function that calls itself
#modules are used to separate code in separate files and reuse it in other files. A module is a file containing Python code to perform a specific task. It can define functions, classes, and variables. A module can also include runnable code.
# import standard math module 
'''import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)'''

# import module by renaming it
'''import math as m

print(m.pi) # Output: 3.141592653589793'''

#the dir() function is used to list all the function names in a module.
'''import math
print(dir(math)) '''# Output: ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', ...]

#main() function is the execution point of a program file. It is the first function that is executed when a program is run. It is not a built-in function in Python, but it is a convention to define a main() function in a program file. The main() function is usually defined at the end of the program file and is called at the end of the file to start the execution of the program.
#The __name__ variable is a special builtin Python variable that shows the name of the current module.
'''print(__name__)'''
'''import practice''' #this prints the contents in practice.py file

# A directory is a collection of files and subdirectories
'''import os

print(os.getcwd()) '''#getcwd gets the current directory in for of a string

#importing a csv file and reading it using the csv module. The csv module is used to read and write CSV files. It provides functionality to both read from and write to CSV files. The csv.reader() function is used to read a CSV file. It takes a file object as an argument and returns a reader object that can be iterated over to get the rows of the CSV file.
'''import csv

with open('people.csv', 'r') as file: #opened the people.csv file in reading mode
    reader = csv.reader(file) #used the csv.reader() function to read the file.

    for row in reader:
        print(row)'''
        
'''import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])#creates a protagonist.csv file and used csv.write to write to the file
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])'''
    

#how objects access attributes of a class
'''class Bike:
    name = ""
    gear = 0
Bike1 = Bike()
Bike1.name = "Yamaha"
Bike1.gear = 5
print(Bike1.name) #prints Yamaha
print(Bike1.gear) #prints 5'''


'''class Animal:

    # attributes and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        
        super().eat() # call the eat() method of the superclass using super()
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()'''

#polymorphism means a single method can be used to carryout different operations. forexaple + can be used to add two numbers or join two strings.

class Vehicle:
    name = "My Vehicle"
    def __init__(self, name):
        self.name = name

vitz = Vehicle("vitz")
print(vitz.name)

rav4 = Vehicle("rav4")
print(rav4.name)
