# A function is a block of code which only runs when it is called.
# In Python, we do not use curly brackets, we use colon in place of curly brackets
# and indentation with tabs or spaces
# function is defined using def keyword

# Create function
def my_function():
  print("Hello from a function")

my_function()

#Calling a function and passing arguments
def sayHello(name):
    print(f'Hello {name}')

sayHello('John Doe')

# Create function with default value
def sayHello1(name='Sam'):
    print(f'Hello {name}')

sayHello1()#Run without argument

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num=getSum(10, 3)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression. Very similar to JS arrow functions

getSum1 = lambda num1, num2: num1 + num2
print(getSum1(11, 4))

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Arbitrary Keyword Arguments, **kwargs
#if the number of keyword arguments is unknown,add a double ** before the parameter name:
#This way the function will receive a dictionary of arguments,
# and can access the items accordingly:

def my_function2(**kid):
  print("His last name is " + kid["lname"])

my_function2(fname = "Tobias", lname = "Refsnes")

#Keyword Arguments
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function3(child3,child2, child1):
  print("The youngest child is " + child1)

my_function3(child1 = "Gmail", child2 = "Paul", child3 = "Linda")

#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function4(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function4(fruits)

#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function
# definition with no content, put in the pass statement to avoid getting an error.

def myfunction5():
  pass

#Recursion
#Python also accepts function recursion, which means a defined function can call itself.
#Recursion is a common mathematical and programming concept.
#It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.
#The developer should be very careful with recursion as it can be quite easy to slip
#into writing a function which never terminates, or one that uses excess
#amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
#To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)