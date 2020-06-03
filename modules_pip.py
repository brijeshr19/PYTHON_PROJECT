#PIP is a package manager for Python packages, or modules if you like.
#Modules are Python code libraries you can include in your project.

#Check if PIP is Installed
#Navigate your command line to the location of Python's script directory,
# and type the following:
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

#Install PIP
#If you do not have PIP installed, you can download and install
# it from this page: https://pypi.org/project/pip/

#Install package
#If camelcase module not there then install with command
# Command: C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase

#Find Packages
#Find more packages at https://pypi.org/.

#Remove a Package
#Use the uninstall command to remove a package
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

# To check what modules are installed use command
# Command: pip freeze

#List Packages
#Use the list command to list all the packages installed on your system:
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list

import camelcase
c=camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

from camelcase import CamelCase
c1 = CamelCase()
print(c1.hump('hello there world'))

#Download and Install MySQL connector
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root123")

