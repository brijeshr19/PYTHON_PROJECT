from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(8):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(8):
            print('Hi')
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)#This sleep will allow to print one by one Hello and Hi
t2.start()

#Here bye will be executed by main thread
print('Bye')

print('***************************')
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(8):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(8):
            print('Hi')
            sleep(1)

t1= Hello()
t2= Hi()

t1.start()
sleep(0.2)#This sleep will allow to print one by one Hello and Hi
t2.start()

#join() will wait for t1 and t2 thread to complete after that execute main thread print()
t1.join()
t2.join()

print('doodle')

