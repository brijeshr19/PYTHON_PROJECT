#Indentation
#Python relies on indentation (whitespace at the beginning of a line)
# to define scope in the code. Other programming languages often use
# curly-brackets for this purpose.

#a = 33
#b = 200
#if b > a:
#print("b is greater than a") # you will get an error

x = 21
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
  print(f'{x} is greater than {y}')

#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
if x > y:print(f'{x} is greater than {y}')

# If/else
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{y} is greater than {x}')  

# elif:The elif keyword is pythons way of saying "if the previous conditions were not true,
# then try this condition".
# The else keyword catches anything which isn't caught by the preceding conditions.
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')  
else:
  print(f'{y} is greater than {x}')

#You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements
# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
    print(f'or operator....{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'not operator....{x} is not equal to {y}')


# Membership Operators (not, not in) -
# Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]
z = 4
#  in
if z in numbers:
  print(z in numbers)#true. This will compare 4 in numbers
  print(f'in operator....{z} in numbers')# this will print 4 as it is and do not compare

# not in
if x not in numbers:
  print(x not in numbers)#true. This will compare 21 not in numbers
  print(f'not in operator....{x} in numbers')# This will print 21 as it is and do not compare

# Identity Operators (is, is not) - Compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

t=3
p=4

# is statement
if t is p:
  print(f'is operator')
  print(t is p)#false

# is not statement
if t is not p:
  print(f'is not operator')
  print(t is not p)#true

#pass statement
#if statements cannot be empty, but if you for some reason have an if statement
# with no content, put in the pass statement to avoid getting an error.

l = 33
m = 200

if m > l:
  pass

