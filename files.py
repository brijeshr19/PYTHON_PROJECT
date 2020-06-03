# Python has functions for creating, reading, updating,deleting files.

#Create a New File/Open a file
#To create a new file in Python, use the open() method.
#The open() function takes two parameters; filename, and mode
#There are 4 different modes for opening a file:
# "r" - Read - Default value. Opens a file for reading, I/O error if the file does not exist
# "a" - Append - Opens a file for appending, creates the new file if it does not exist
# "w" - Write - Opens a file for writing, creates the new file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

#Creates the specified file, returns an error if the file already exists (x mode)
#Result: a new empty file is created!
#myFile = open('myfile.txt', 'x')

#Opens a file for writing, creates the new file if it does not exist(w mode)
myFile = open('myfile.txt', 'w')
myFile.write("I love Python")
myFile.write(" and JavaScript")

# Get some info of file
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#Note: You should always close your files, in some cases because due to buffering,
#changes made to a file may not show until you close the file.
myFile.close()

#Opens a file for appending, creates the new file if it does not exist
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.write(' and I like Net')
myFile.write(' and I like JavaScript')
myFile.write(' and I like Python')
myFile.write(' and I like C')
myFile.write(' and I like C++')
myFile.write(' and I like NodeJS')
myFile.write(' and I like ReactJS')
myFile.write(' and I like NextJS')
myFile.write(' and I like NextJS')
myFile.close()

# Reading from file

# myFile = open("demofile.txt")#if mode not supplied then it will default take r

# Below statement is same as above
# myFile = open("demofile.txt", "rt")#Because "r" for read, and "t" for text are the default values

#"r" - Read - Default value. Opens a file for reading, I/O error if the file does not exist
myFile = open('myfile.txt', 'r')

#By default read() method returns the whole text,
stext = myFile.read()
print(stext)
myFile.close()

#Another way to read whole text
#By looping through the lines of the file, you can read the whole file, line by line:
stext1 = open('myfile.txt', 'r')
for x in stext1:
    print(x)

#Read Parts of file
#Specify how many characters you want to return
myFile = open('myfile.txt', 'r')
text = myFile.read(100) #Read only first 100 characters
print(text)


