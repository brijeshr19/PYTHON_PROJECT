#A List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Set is a collection which is unordered and unindexed. No duplicate members.

#Dictionary(Map) is a collection which is unordered, changeable and indexed.
# No duplicate members. In place of index number we use keys

#Dictionaries has curly brackets, and they have keys and values.
#Dictionaries are similar to Objects in JS

# Create Dictionary object
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person,type(person))

# Use dict() Constructor
person2 = dict(first_name='Sara', last_name='Williams',age=50)
print(person2,type(person2))

# Accessing Items
# You can access the items of a dictionary by referring to its key name,
# inside square brackets:
x = person['first_name']
print(x)

#Other way
print(person['first_name'])

# Method get() will give you the same result:
print(person.get('last_name'))

#Change Values. Dictionay values are Changeble
#You can change the value of a specific item by referring to its key name:
person["age"] = 50
print(person)

# Add key/value to dictionary
# Adding an item to the dictionary is done by using a new index key
# and assigning a value to it:
person['phone'] = '555-555-5555'

# Copy dictionary- copy() method
# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1, and changes made
# in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary
# method copy().

# Changing person age from 50 to 70 will effect person2
person2=person
person["age"] = 70
print(person2)#{'first_name': 'John', 'last_name': 'Doe', 'age': 70, 'phone': '555-555-5555'}

# Changing person age from 70 to 100 will not effect person2
person2 = person.copy()
person["age"] = 100
print(person2)#{'first_name': 'John', 'last_name': 'Doe', 'age': 70, 'phone': '555-555-5555'}

# Change dictionary value. It will not affect original person
person2['first_name'] = 'Catherine'
print(person2)#{'first_name': 'Catherine', 'last_name': 'Doe', 'age': 70, 'phone': '555-555-5555'}
print(person)#{'first_name': 'John', 'last_name': 'Doe', 'age': 100, 'phone': '555-555-5555'}

#Another way to make a copy is to use the built-in method dict().
person3 = dict(person)
print(person3)#{'first_name': 'John', 'last_name': 'Doe', 'age': 100, 'phone': '555-555-5555'}

# Get dictionary keys
print(person.keys())#dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get dictionary items(both key/values)
print(person.items()) #dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 100), ('phone', '555-555-5555')])

#Check if specified Key Exists using in keyword
if "age" in person:
  print("Yes, 'age' is one of the keys in the person dictionary")

#Removing Items
# Remove single item using del and pop
del(person['age'])

#The pop() method removes the Single item with the specified key name
person.pop('phone')
print(person)#{'first_name': 'John', 'last_name': 'Doe'}

#The popitem() method removes the last inserted item
#(in versions before 3.7, a random item is removed instead)
person.popitem()#removes last item
print(person)#{'first_name': 'John'}

# Clear empties Dictionaries clear() method
person.clear()
print(person)#{} empty list

#del keyword. The del keyword can also delete the dictionary completely:
del person
#print(person) #this will cause an error because "thisdict" no longer exists.

# Get length
print(len(person2))#4

# List of dictionary (multidimensional array of dictionary)
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
print(people,type(people))# [{'name': 'Martha', 'age': 30}, {'name': 'Kevin', 'age': 25}] <class 'list'>
print(people[1]['name'])#Kevin. people[1] represent first row

#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary,
#but there are methods to return the values as well.

#Print all key names in the dictionary, one by one
for x in person2:
  print(x)#first_name last_name age phone

#Print all values in the dictionary, one by one:
for x in person2:
  print(person2[x])#John Doe 100 555-555-5555

#Use values() function to return values of a dictionary
for x in person2.values():
  print(x)#John Doe 100 555-555-5555

#Loop through both keys and values, by using the items() function:
for x, y in person2.items():
  print(x, y)#first_name John last_name Doe age 100 phone 555-555-5555


