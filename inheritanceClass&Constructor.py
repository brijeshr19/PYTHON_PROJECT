# Class Inheritance allows us to define a sub class that inherits all the methods
# and properties from parent class.
#Python Supports multiple Inheritance

#Note:Subclass can access all feature of Superclass but
#Superclass can not access all features of Subclass

#Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Im in parent class constructor')

    def printname(self):
        print(self.firstname, self.lastname)

#Subclass
#Send the parent class as a parameter when creating the child class:
class Student(Person):
    #When you add the __init__() function, the child class will no longer
    #inherit the parent's __init__() function.
    #It means The child's __init__() function overrides the inheritance of the parent's
    # __init__() function.

    def __init__(self, fname, lname, year):
        print('Im in child class constructor')
        #Person.__init__(self, fname, lname) #this is not used now
        super().__init__(fname, lname)#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
        self.graduationyear = year

    #If you add a method in the child class with the same name as a function
    #in the parent class, the inheritance of the parent method will be overridden.
    def welcome(self):
       print("Welcome", self.firstname, self.lastname, self.graduationyear)

#Calling Child class constructor  __init()__ function
x = Student("Mike", "Olsen", 2019)

#Calling graduationyear attribute of child class
print(x.graduationyear)#2019

#Calling printname() method of parent class
x.printname() #Mike Olsen

#Calling Child class welcome() function
x.welcome()#Welcome Mike Olsen 2019

print('*************Multiple Inheritane in Python**************')
class A:
    def feature1(self):
        print('Feature1 is working')

    def feature2(self):
        print('Feature2 is working')

#Single Inheritance
class B(A):
    def feature3(self):
        print('Feature3 is working')

    def feature4(self):
        print('Feature4 is working')

class C:
    def feature5(self):
        print('Feature5 is working')

#Multiple Inheritance. A and C has no relation but inherited by D
class D(A,C):
    def feature6(self):
        print('Feature6 is working')

a1Obj= A()

a1Obj.feature1()
a1Obj.feature2()

#Single Inheritance Features. Since B inherit A
b1Obj=B()
b1Obj.feature1()
b1Obj.feature2()
b1Obj.feature3()
b1Obj.feature4()

#Multiple Inheritance. Since D inherit A and C
d1Obj = D()
d1Obj.feature1()
d1Obj.feature2()
d1Obj.feature5()
d1Obj.feature6()

print('*********Constructor Inheritance calling __init(self)__ of  parent only***********')
class X:
    def __init__(self):
        print('in __init__ X')#in __init__ X

    def feature1(self):
        print('Feature1 is working')

    def feature2(self):
        print('Feature2 is working')

#Single Inheritance
class Y(X):
    def feature3(self):
        print('Feature3 is working')

    def feature4(self):
        print('Feature4 is working')

#This is will automatically call constructor of X since Y donot have Constructor
y1Obj = Y()

print('******Constructor Inheritance calling __init(self)__ of  child only******')
class P:
    def __init__(self):
        print('in __init__ P')

    def feature1(self):
        print('Feature1 is working')

    def feature2(self):
        print('Feature2 is working')

#Single Inheritance
class Q(P):
    def __init__(self):
        print('in __init__ Q')#in __init__ Q

    def feature3(self):
        print('Feature3 is working')

    def feature4(self):
        print('Feature4 is working')

#This is will automatically call constructor of X since Y donot have Constructor
q1Obj = Q()

print('******Constructor Inheritance calling __init(self)__ of  parent and child both******')
class L:
    def __init__(self):
        print('in __init__ L')

    def feature1(self):
        print('Feature1 is working')

    def feature2(self):
        print('Feature2 is working')

#Single Inheritance
class M(L):
    def __init__(self):
        super().__init__()
        print('in __init__ M')#

    def feature3(self):
        print('Feature3 is working')

    def feature4(self):
        print('Feature4 is working')

#This will call __init__(self) of L first and then __init__ if M as super() is used
m1Obj = M()#in __init__ L in __init__ M

print('******Method Resoulution Order(MRO)******')
#When
class E:
    def __init__(self):
        print('in __init__ E')

    def feature1(self):
        print('Feature1-A is working')

    def feature2(self):
        print('Feature2 is working')

#No Inheritance
class F:
    def __init__(self):
        print('in __init__ F')#

    def feature1(self):
        print('Feature1-F is working')

    def feature2(self):
        print('Feature2 is working')

#Multiple Inheritance. Since G has 2 superclasses
class G(E,F):
    def __init__(self):
        #This super() will call E as it consider from left to right order
        super().__init__()
        print('in __init__ G')#

    def feat(self):
        super().feature1()
        print('Feature5-G is working')


g1Obj = G() #in __init__ E in __init__ G. Left to right concept
g1Obj.feat()#Feature1-A is working. Feature5-G is working.Left to Right concept in MRO