#Instance Methods
#Class Methods @classmethod
#Static Methods @staticmethod

#getter and setter are use in place of constructors
#getter are accessors and setters are called mutators

class Student:

    school ='Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #Instance methods
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def staticInfoMethod():
        print('this is Student class static method')

s1 = Student(15,20,25)
s2 = Student(30,40,50)

print(s1.avg())
print(s2.avg())
print(Student.info())
Student.staticInfoMethod()

print('**********Compare Objects of Same Class***************')
class Computer:
    def __init__(self):
        self.name = 'Navin'
        self.age = 30

    # Here c1 become self and c2 becomes other compare()
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print('They are Same')
else:
    print('They are different')

c1.age =20

#Here c1 become self and c2 becomes other compare()
if c1.compare(c2):
    print('They are Same')
else:
    print('They are different')

print('**********getter and setter methods***************')
#getter and setter are use in place of constructors
#getter are accessors and setters are called mutators
class College:

    school ='Telusko'

    #This is optional --init__. If we do not use it then too it  will work
    def __init__(self):
        pass

    # def __init__(self,m1,m2,m3):
    #     self.m1 = m1
    #     self.m2 = m2
    #     self.m3 = m3

    #Instance methods
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def get_m2(self):
        return self.m2

    def get_m3(self):
        return self.m3

    def set_m1(self,value):
        self.m1 = value

    def set_m2(self,value):
        self.m2 = value

    def set_m3(self,value):
        self.m3 = value

#Not initializing using constructor
# col = College(15,20,25)
# col2 = College(30,40,50)

#Blank Constructor
col3 =College()
col4 =College()
col5 =College()

col6 =College()
col7 =College()
col8 =College()

#Calling setter
col3.set_m1(15)
col4.set_m2(20)
col5.set_m3(25)

#printing getter
print(col3.get_m1())
print(col4.get_m2())
print(col5.get_m3())

#Calling setter
col6.set_m1(30)
col7.set_m2(40)
col8.set_m3(50)

#printing getter
print(col6.get_m1())
print(col7.get_m2())
print(col8.get_m3())

print('**********getter and setter methods using Property*********')
class School:

    #This is optional __init__. If we do not use it then too it  will work
    def __init__(self):
        pass

    #Using property decorator a getter function @property

    @property
    def age(self):
        return self.m1

    # a setter function

    @age.setter
    def age(self,value):
        self.m1 = value

#Blank Constructor
sch3 =School()
sch4 =School()

#Calling setter
sch3.age=20

#printing getter
print(sch3.age)

#Calling setter
sch4.age=30

#printing getter
print(sch4.age)