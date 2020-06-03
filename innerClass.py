#Inner Classes
#You can create Object of Inner Class inside outer class
#You can create Object of Inner Class outside the Outer class
#provided you use Outer Class name to call it.

class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() #First Way: create Object of Inner Class inside outer class

    def show(self):
        print(self.name,self.rollno) #Navin 2001
        self.lap.show()#HP i5 8

    #Inner Class declaration
    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self) :
            print(self.brand,self.cpu,self.ram)

s1 = Student('Navin',2001)
s2 = Student('Raj',2002)

#Accession inner class Object
print(s1.lap.brand)#HP

lap1Obj = s1.lap
lap2Obj = s2.lap

print(id(lap1Obj),id(lap2Obj))#2 dofferent Ids you will get

s1.show()#Navin 2001 HP i5 8

#Create Object of Inner Class outside the Outer class
lap3Obj = Student.Laptop()
lap3Obj.show()#HP i5 8
