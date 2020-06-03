#A for loop is used for iterating over a sequence
#(that is either a list, a tuple, a dictionary, a set, or a string).

#list
people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for in loop
for x in people:
  print(f'Current Person list: {x}')

# Break
for x in people:
  if x == 'Sara':
    break
  print(f'Current Person break: {x}')#This is outside if loop so print#John Paul

#Continue
#With the continue statement we can stop the current iteration of the loop,
#and continue with the next.
for x in people:
  if x == 'Sara':
    continue
  print(f'Current Person continue: {x}')#This is outside if loop so print# John Paul Susan

#range() function
#To loop through a set of code a specified number of times,
#we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default,
#and increments by 1 (by default), and ends at a specified number.

#This will print 0 to 5
for x in range(6):
  print(x)

#This will print people from 0 to 4
for i in range(len(people)):
  print('range', people[i])
  print(f'range {people[i]}')

#This will print 0 to 10
for i in range(0, 11):
  print(f'Number: {i}')

#The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter:
# range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed
# when the loop is finished
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nested Loops
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content,
#put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass

# While loops execute a set of statements as long as a condition is true.
count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1

#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters
for x in "banana":
  print(x)