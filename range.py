#Python range() Function
#The range() function returns a sequence of numbers, starting from 0 by default,
#and increments by 1 (by default), and stops before a specified number.

# Syntax
# range(start, stop, step)

#Create a sequence of numbers from 0 to 5, and print each item in the sequence
x = range(6)
for n in x:
  print(n)

#Create a sequence of numbers from 3 to 5, and print each item in the sequence:
x = range(3, 6)
for n in x:
  print(n)

#Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
x = range(3, 20, 2)
for n in x:
  print(n)

z=list (range(10))
print(z)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#list
people = ['John', 'Paul', 'Sara', 'Susan']

#Taking length of list
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