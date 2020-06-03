# Python is an object oriented programming language.
# Almost everything in Python is an object
# An object has properties and methods(functions) associated with it.

# A Class is like a blueprint for creating objects.
# A Class is like an object constructor.

#Self Parameter (ref to Current instance of class)
#The Self Parameter is reference to the current instance of the Class,
#and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like,
#but it has to be the first parameter of any function in the class:

#Create class use the keyword class
class User:
  #Global Variable
  x = 5
  # Constructor. All classes have a built-in function called __init__(),
  # which is always executed when the class is being initiated.
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.x = 10 #variable
    print(f'User class Constructor is called with {self.name} {self.age} {self.email} and variable {self.x}')

  # Method1
  def has_birthday(self):
    self.age += 1

  #Method2
  def greeting(self):
    return f'User Class greeting method called. My name is {self.name} age is {self.age} and {self.x}'

#Note Here Indenting is important. If you do wrong indenting it will not work
#Init User object (calling constructor)
userObj = User('Brad Traversy','brad@gmail.com',37)
userObj.has_birthday()
print(userObj.greeting())
print(userObj.x)#10. print global var

#Modify Object Properties
#You can modify properties on objects like this
userObj.x = 40
print(userObj.x)#40. print global var

#Delete Object Properties (del)
del userObj.age
#print(userClass.age)

#Global variables cannot be deleted
del userObj.x
print(userObj.x)#5. print global var

#Delete Objects itself
#You can delete objects by using the del keyword:
del userObj
#print(userClass) #this will give error

# The pass Statement.class definitions cannot be empty,
# but if you for some reason have a class definition empty,
# then put the pass statement to avoid getting an error.
class Person:
  pass

# Extending class (User)
class Customer(User):
  # Global Variable
  y = 10

  # Constructor. All classes have a built-in function called __init__(),
  # which is always executed when the class is being initiated.
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0 #Variable
    print(f'Customer class Constructor Called {self.name} {self.age} {self.email} and {self.balance}')

  #Method
  def set_balance(self, balance):
    self.balance = balance

  #Note if this greeting method is commented then super class greeting called
  #Method
  def greeting(self):
    return f'Customer Class greeting method called.My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#Note Here Indenting is important.
# If you do wrong indenting it will not work

#Init customer object(calling Constructor)
customerClass = Customer('Janet Johnson', 'janet@yahoo.com', 25)
customerClass.set_balance(500)
print(customerClass.greeting())

print('*************************')

class Computer:

  def __init__(self):
    self.name='Navin'
    self.age = 28

  def update(self):
    self.age = 30

  def compare(self,other):
    if (self.age==other.age):
      return True
    else:
      return False

c1 = Computer()
c2 = Computer()

c1.name = 'Rashi'
c1.age = 12

c1.update()

if c1.compare(c2):
  print("They are same")
else:
  print("They are different")

print(c1.name)#Rashi
print(c1.age)#30
print(c2.name)#Navin
print(c2.age)#28

print('*******Global(Class Namespace) and Local(Instance Namespace)********')

class Car:

  wheels = 4 #Class namespace

  def __init__(self):
    self.mil = 10 #Instance Namespace
    self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5 #Global or Class Namespace can be accesses with classname

print(c1.com,c1.mil, c1.wheels)
print(c2.com,c2.mil, c2.wheels)



