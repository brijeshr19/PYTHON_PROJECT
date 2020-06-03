#Polymorphism Types
#Duck Typing
#Operator Overloading
#Method Overloading
#Method Overriding

#Duck Typing Polymorphism
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')

class VsCode:
    def execute(self):
        print('SpellCheck')
        print('ConventionCheck')
        print('Compiling')
        print('Running')

class Laptop:
    def code(self,ide):
        ide.execute()

ide = PyCharm()
lap1 = Laptop()
#Passing ide of PyCharm
lap1.code(ide)

ide = VsCode()
lap2 = Laptop()
#Passing ide of VsCode
lap2.code(ide)

#Operator Overloading
#Whenever you do addition substraction deletion you are calling methods behind the
#scene like(+) __add__(self,other),(-) __sub__(self,other),(*) __mul__(self,other),
#()/ __div__(self,other),(<) __It__(self,other),(>) __gt__(self,other),(>=)__ge__(self,other)

#If you want to perform any operation on User Defined Objects then you need
#to define methods of your own like for Student object

a= 5
b= "hello"
#print(a+b)#unsupported operand type(s) for +: 'int' and 'str'

x= 5
y= 6

print(x+y)#11
#behind the scene below is working actually
print(int.__add__(x,y))#11

p='Hello'
q='World'
print(p+q)#HelloWorld
#behind the scene below is working actually
print(str.__add__(p,q))#HelloWorld

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    #Here s1 is self and s2 is other
    def __add__(self, other):
        z1 = self.m1+other.m1
        z2 = self.m2+other.m2
        s3= Student(z1,z2)
        return s3

    def __gt__(self, other):
        t1 = self.m1+self.m2
        t2 = other.m1+other.m2

        if t1>t2:
            return True
        else:
            return False

    #Object to Value conversion
    def __str__(self):
        #return '{} {}'.format(self.m1,self.m2)
        return f'{self.m1},{self.m2}'

s1 = Student(20,30)
s2 = Student(40,50)

#When we have not defined add method for s1 and s2 so it will give error
#s3 = s1+s2 #typeError: unsupported operand type(s) for +: 'Student' and 'Student'

#If we Overload operator + with def __add__(self, other): then below result
s3 = s1+s2
print(s3.m1)#60
print(s3.m2)#80

#Another Example
#Comparing s1 and s2 with > operator
if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')

#printing object itself s1
# def __str__(self):
print(s1)#20,30
print(s2)

#Method Overriding
#Method having same Name and same Signature in parent and child class
print('**********Method Overriding*********')
class A:
    def show(self):
        print('in A show')

class B:
    def show(self):
        print('in B show')

a1 = B()
a1.show()

#Method Overloading
#Single method in any class (parent or child) having same name
# and arguments having None with if condition
print('**********Method Overloding*********')
class College:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        return s

s1=College(55,60)

print(s1.sum(5,10,15))
print(s1.sum(5,10))
print(s1.sum(5))


