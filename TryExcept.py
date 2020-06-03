#Python Try Except
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the
#try- and except blocks.

#try block will generate an exception, because x is not defined:
#Since the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error
#This statement will raise an error, because x is not defined:
#print(x)
try:
  print(x)
except:
  print("An exception occurred")

#Many Exceptions
#You can define as many exception blocks as you want
#Print one message if the try block raises a NameError and another
#for other errors:

try:
  print(z)
except NameError:
  print("Variable z is not defined")
except:
  print("Something else went wrong")

#Else block with try and except
#You can use the else keyword to define a block of code to be executed
#if no errors were raised.
#In this example, the try block does not generate any error.

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print('***************try except finally****************')
#Finally with try and except
#The finally block, if specified, will be executed regardless
# if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#try to open and write to a file that is not writable
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  print("Finally block")

print('***************raise exception****************')
#Raise an exception
#The raise keyword is used to raise an exception.
#You can define what kind of error to raise, and the text to print to the user.

#Raise an error and stop the program if x is lower than 0
x = -1
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except:
    print("Exception raised manually")

#Raise a TypeError if y is not an integer
y = "hello"
try:
    if not type(y) is int:
        raise TypeError("Only integers are allowed")
except:
    print("Exception raised manually")

