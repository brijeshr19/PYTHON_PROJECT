# Strings in python are surrounded by either single('') or double quotation("") marks.
# Strings in Python is immutable you cannot change the value of String in Python
# once assigned)

name = 'Brad'
age = 37

# Concatenate
#print('Hello, my name is ' + name + ' and I am ' + age) #This will give error as String and num can not be concatinated
print('Hello, my name is ' + name + ' and I am ' + str(age)) #This is correct

# String Formatting
# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = "helloworld"

# Capitalize method for string. This will capitalize forst letter only
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace. This will not affect original string
print(s.replace('world', 'everyone'))
print(s)#Will print Original String only helloworld
# Count
x = 'h'
print(s.count(x))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('rld'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())#False

#Telusko Strings
teluskoStr='youtube'

print(teluskoStr[0])#y

#print(teluskoStr[8])#IndexError: string index out of range

print(teluskoStr[-1])#e. It will start with end
print(teluskoStr[-2])#b

#print first 2 characters
print(teluskoStr[0:2])#yo

print(teluskoStr[1:4])#out

#printing from 1 till end
print(teluskoStr[1:])#outube

#print from 0 till 4
print(teluskoStr[:4])#yout

#print from 3 till end. 10 is out of range
print(teluskoStr[3:10])#tube

#Changing String not possible
teluskoStr[0]='m'#TypeError: 'str' object does not support item assignment






