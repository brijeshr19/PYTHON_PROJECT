#Creating Variables
#Variables are containers for storing data values of various types
#A Variable is created the moment you first assign a value to it.
#Variables do not need to be declared with any particular type and
#Variable type can be changed after they have been set.

# Variable are of 2 Types:
# Instance Variable
# Class (Static) Variables

#Namespace is area where you create/store Object and Variables
#Class Namespace or Global
#Object/Instance Namespaces or Local

'''
This is a multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one. A variable name cannot start with a number
"""
#Single Assignment
x = 1           # int
y = 2.5         # float
name = 'John'   # str
is_cool = True  # bool

# Multiple assignment (Either use round brackets)
x, y, name, is_cool = (1, 2.5, 'John', True)

#Multiple assignment
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

##And you can assign the same value to multiple variables in one line
l = m = n = "Strawberry"
print(l,m,n)

# Basic math
a = x + y
print(x, y, name, is_cool, a)

# Casting
#integer to String
x = str(x)
print(type(x), x) #<class 'str'> 1
print(x)#x not affected

#Concatinate String
b='navin'
c='singh'
a = b+c
print(a)#navinsingh

#If you try to combine a string and a number, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

#float to int
t = int(y)
print(type(t), t)#<class 'int'> 2
print(y)#y not affected

#int to float
z = float(x)
print(type(z), z)
print(x)#x not affected

print(8/4)#2.0
print(8//4)#2 Integer division
print(5/2)#2.5
print(5//2)#2. Integer division
print(10%3)#1

#Variables do not need to be declared with any particular type
#and can even change type after they have been set.
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

#Global Variables or Class Namespace
#Variables that are created outside of a function
# (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function.
# Global variable with the same name will remain as it was,
# global and with the original value.

e = "awesome"#Global variable or Class Namespace

def myfunc():
  e = "bekar" #Local varible Instance
  print("Python is " + e)#Python is bekar

myfunc()

print("Python is " + e)#Python is awesome

#The global Keyword
#Normally, when you create a variable inside a function that variable is local,
# and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

p = "laundery" #Global variable or Class Namespace
def myfunc():
  global p #Now it will change Global variable inside Function
  p = "fantastic"
  print("Python is " + p)#Python is fantastic

myfunc()
print("Python is " + p)#Python is fantastic

print('*******Global(Class Namespace) and Local(Instance Namespace)********')

class Car:

  wheels = 4 #Class namespace

  def __init__(self):
    self.mil = 10 #Instance Namespace
    self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print(c1.com,c1.mil, c1.wheels)
print(c2.com,c2.mil, c2.wheels)

