#A List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Difference between List and Tuples is that List is Changeble and Tuples are unchangeable(immutable)
#Iteration in tuple is faster than List

print('********Tuple************')
# Create tuple (containing round braces)
fruits = ('Apples', 'Oranges', 'Grapes')
print(fruits)

# Using a tuple constructor
fruits1 = tuple(('Chiku', 'Pomgranetae', 'Strawberries'))
print(fruits1)

#Check if in Tuple
if 'Apples' in fruits:
    print(True)

# Single value in tuple is treated as type String
fruits2 = ('Apples')
print(fruits2,type(fruits2))#Apples <class 'str'>

# Single value needs trailing comma treated as tuple
fruits3 = ('Apples',)
print(fruits3,type(fruits3))#('Apples',) <class 'tuple'>

# Get value of tuple index
print('Get value of fruits by index',fruits[1])

# Can't change value. Unchangebale
#fruits[0] = 'Pears'
#print(fruits)

#Counting tuple
fruits.count(fruits)
print('Counting fruits',fruits)

# Append 'Apple' at the end of tuple. Duplicate tuple
fruits = fruits + ('Apple' ,)
print(fruits)

#Adding items in a specific index. But this will remove trailing items after ivory
fruits = fruits[:1] + ('ivory',)
print(fruits)

#Adding items in a specific index. Add trailing items required
fruits = fruits[:1] + ('Strawberry',)+('blackberry',)+fruits[:1]
print(fruits)

# Get length
print(len(fruits))

# Delete complete tuple. tuple does not support single item deletion like dictionaries
#del(person['age']) #wrong statement
#person.pop('phone')#wrong statement
del fruits2
#print(fruits2) #This will give error as fruits2 delete

#SET
# A Set is a collection which is unordered and unindexed. No duplicate members.

print('********SET************')
# Create set (Set has curly brackets)
fruits_set = {'Apples', 'Oranges', 'Mango'}
print(fruits_set)
# Create set by constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Check if in set
print('Apples' in fruits_set)

#Loop values
for x in fruits_set:
  print(x)

# Add to set. Set is unordered so it added anywhere
#To add one item to a set use the add() method.
fruits_set.add('Grape')
print(fruits_set)

#To add more than one item to a set use the update() method.
fruits_set.update(["orange", "mango", "grapes"])
print(fruits_set)

#Join Two Sets
#You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

#Update()
set1 = {"e", "f" , "g"}
set2 = {4, 5, 6}

set1.update(set2)
print(set1)

set3 = set1.union(set2)
print(set3)

#print(fruits_set[2]) #Unindexed

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

#Another method to remove discard()
fruits_set.discard("banana")

#Remove last item by pop()
x = fruits_set.pop()
print(x)
print(fruits_set)

# Add duplicate. No duplicates allowed and ignored
fruits_set.add('Apples')
print(fruits_set)# This will be ignored

#Length len()
print(len(fruits_set))

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete
del fruits_set
#print(fruits_set) #This will give error
