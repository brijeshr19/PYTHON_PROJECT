#A List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Arrays
#Note: Python does not have built-in support for Arrays,
#but Python Lists can be used instead.

# Create list with single row(Containing the curly brackets)
print('List')
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(numbers)
print(fruits)

print('List Constructor')
# Use a list constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers2)

print('Multidimesional List')
#Multidimensional list
numbers3 = [
    {1, 2, 3, 4, 5},
    {7, 8, 9, 10, 11}
]

print(numbers3,type(numbers3))

#Access Items
#You access the list items by referring to the index number
print(fruits[1])#Oranges

#Negative Indexing
print(fruits[-1])#Pears

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
print(fruits[2:5])#['Grapes', 'Pears'] Since range ends at 3

#By leaving out the start value, the range will start at the first item:
print(fruits[:3])#['Apples', 'Oranges', 'Grapes']

#This example returns the items from "Grapes" and to the end:
print(fruits[2:])#['Grapes', 'Pears']

# List Length
# To determine how many items a list has, use the len() function:
print(len(fruits))#4

# Change Item Value
# To change the value of a specific item, refer to the index number:
fruits[0] = 'Blueberries'
print('Changing vale at 0 index',fruits)#['Blueberries', 'Oranges', 'Strawberries', 'Pears', 'Mangos']

#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword
if 'Blueberries' in fruits:
  print("Yes, 'Blueberries' is in the fruits list")

# Append to list
#To add an item to the end of the list, use the append() method:
fruits.append('Mangos')
print('Appending fruit Mango',fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print('Inserting fruit Strawberries',fruits)

# Remove from list
#The remove() method removes the specified item:
fruits.remove('Grapes')
print('Removing fruit Grapes',fruits)

# Remove with pop
#The pop() method removes the specified index, (or the last item if index is not specified):
fruits.pop(2)
print('Remove with pop(2)',fruits)

#pop() will remove the last item
fruits.pop()
print(fruits)

#Duplicates elements
fruits.append('Oranges')
print('Duplicate Oranges',fruits)

# Reverse list
fruits.reverse()
print('Reverse fruits order',fruits)

# Sort list
fruits.sort()
print('Sort fruits ascending',fruits)

# Reverse sort
fruits.sort(reverse=True)
print('Sort fruits Reverse',fruits)

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().

mylist = fruits.copy()
print('Copy list using copy()',mylist)

#Another way to make a copy is to use the built-in method list().
mylist1 = list(fruits)
print('Copy list using list()',mylist1)

#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Use the extend() method, which purpose is to add elements from one list to another list
list3 = ["x", "y" , "z"]
list4 = [4, 5, 6]

list3.extend(list4)
print(list3)

#The clear() method empties the list:
# fruits.clear()
# print(fruits)#[]

#The del keyword removes the specified index:
del fruits[0]
print(fruits)

#deleting complete list
# del fruits
# print(fruits)

#Iterating list with for loop
print('Iterating list with for loop')
people = ['John', 'Paul', 'Sara', 'Susan']
for i in range(len(people)):
  print('range', people[i])

#Searching element with List using for loop
print('********Searching element with List using for loop****')
pos =-1 #Counter
def search(list,n):
    i=0
    for i in range(len(list)):
        if list[i]==n:
            global pos
            pos=i
            return True
        #i=i+1 #For loop does not require increment

    return False

list = [5,8,4,6,9,2]

#Search 9
n=9

if(search(list,n)):
    print('found at ',pos)
else:
    print('Not found at')

#binarySearch with List using for loop
#For binarySearch values should be sorted fist else it will not work

print('********BinarySearch with List using for loop****')
pos =-1#Counter
def search(list1,n):
    l=0
    u=len(list1)-1

    while l<=u:
        mid = (l+u)//2

        if list1[mid]==n:
            global pos
            pos=mid
            return True
        else:
            if list1[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False #This is inside While

list = [4,7,8,12,45,99,102,702,10997,56666]

#Search 102
n=102

if search(list,n):
    print('found at ',pos+1)
else:
    print('Not found at ')