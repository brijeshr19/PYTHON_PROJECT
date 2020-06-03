#Download and Install MySQL connector
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root123",database="telusko")
print(mydb)

print('******Create Database*******')
#Create Databases
#mycursor = mydb.cursor()#Getting Cursor
#mycursor.execute("CREATE DATABASE mydatabase")

print('******Show Database*******')
#Show Databases
mycursor = mydb.cursor()#Getting Cursor
mycursor.execute('show databases')
for x in mycursor:
  print(x)

# print('******Create Table*******')
# mycursor = mydb.cursor()#Getting Cursor
# # #Create Table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

print('******Show Table*******')
# Check if Table Exists
mycursor = mydb.cursor()#Getting Cursor
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# #Select query
print('*******select student table details******')
mycursor = mydb.cursor()#Getting Cursor
#Select data from Student
mycursor.execute('select * from student')
#Fetch the data using for loop
for i in mycursor:
    print(i)

print('*******select student table details fetchAll******')
# #instead of using cursor directly we will use fetchAll
mycursor.execute('select * from student')
myresult = mycursor.fetchall()
#Fetch the data using for loop
for k in myresult:
    print(k)

print('*******select student table details fetchOne******')
#Using the fetchone() Method
#If you are only interested in one row, you can use the fetchone() method.
#The fetchone() method will return the first row of the result:
mycursor.execute('select * from student')
myresult1 = mycursor.fetchone()
print(myresult1)