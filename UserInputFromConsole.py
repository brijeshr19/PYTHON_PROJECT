#Since x and y are string so string are added
x= input("Enter First Number")
print(type(x))#<class 'str'>
y= input("Enter Second Number")
print(type(y))#<class 'str'>
z=x+y #2+3
print(z)#23

#Convert x and y into int
x= input("Enter First Number")
a=int(x)
y= input("Enter Second Number")
b=int(y)
m=a+b #2+3
print(m)#5

#Alternative of above
x= int(input("Enter First Number"))
y= int(input("Enter Second Number"))
s=x+y #2+3
print(s)

#Getting character from User
ch=input("enter a char") #pqr
print(ch)#pqr

#To print only one character
ch=input("enter a char") #pqr
print(ch[0])#p

#Another way To print only one character
ch=input("enter a char")[0] #pqr
print(ch)#p

#Evaluating expression
result = eval(input("enter a expr"))#1+2-3
print(result)#0


