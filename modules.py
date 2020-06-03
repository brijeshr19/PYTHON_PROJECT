# Modules are Python code libraries you can include in your project.
# Module is a file (with file extension.py) containing a set of functions to include
# in your application.

# Type of Modules?
#(a)There are core python modules (builtin)
#(b)Pip modules:Modules you can install using the pip package manager(including Django)
#(c)Custom modules (created by you)

#Import From Module?
#from keyword is use to import only parts from a module.
#Note: When importing using the from keyword, do not use the module name
#when referring to elements in the module.
#Ex: person1["age"], not mymodule.person1["age"]

# Core modules (builtin)
# import platform
# x = platform.system()
# print(x)

# from keyword is use to import only parts from a module
# from platform import system
# print(system())

# import datetime
# todayDate=datetime.date.today()
# print(todayDate)

#from keyword is use to import only parts from a module
from datetime import date
print(date.today())

import time
todaytimestamp=time.time()
print(todaytimestamp)

#from keyword is use to import only parts from a module
from time import time
todaytimestamp1=time()
print(todaytimestamp1)

import math
x=math.sqrt(25)
print(x)#5.0

z=math.floor(2.4)
print(z)

t=math.floor(2.9)
print(t)

y=math.ceil(2.2)
print(y)

m=math.ceil(2.9)
print(m)

d=math.pow(3,2)
print(d)

e=math.pi
print(e)

#Re-naming a Module
#You can create an alias when you import a module, by using the as keyword:
import mymodule as mx
a = mx.person1["age"]
print(a)








