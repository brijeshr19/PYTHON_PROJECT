# Garbage Collection in Python
# Python’s memory allocation and deallocation method is automatic.
# The user does not have to preallocate or deallocate memory similar to using dynamic memory allocation in languages such as C or C++.
# Python uses two strategies for memory allocation:
#
# (1)Reference counting: Prior to Python version 2.0, the Python interpreter only used reference counting for memory management.
# (2)Garbage collection
#
# Reference counting:
# Reference counting works by counting the number of times an object is referenced by other objects in the system.
# When references to an object are removed, the reference count for an object is decremented.
# When the reference count becomes zero, the object is deallocated.

# Literal 9 is an object
b = 9

# Reference count of object 9 becomes 0.
b = 4

# Ways to make an object eligible for garbage collection

x = []
x.append(1)
x.append(2)

# delete the list from memory or
# assigning object x to None(Null)
del x
# x = None

# Automatic Garbage Collection of Cycles
# Because reference cycles take computational work to discover,
# garbage collection must be a scheduled activity.
# Python schedules garbage collection based upon a threshold of object allocations
# and object deallocations.
# When the number of allocations minus the number of deallocations is greater
# than the threshold number,the garbage collector is run.

# Here, the default threshold on the above system is 700.
# This means when the number of allocations vs. the number of deallocations is greater
# than 700 the automatic garbage collector will run.
# Thus any portion of your code which frees up large blocks of memory is a good candidate
# for running manual garbage collection.

import gc

# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
      gc.get_threshold())

# Manual Garbage Collection
# Invoking the garbage collector manually during the execution of a program
# can be a good idea on how to handle memory being consumed by reference cycles.

# Importing gc module
import gc

# Returns the number of objects it has collected and deallocated
collected = gc.collect()

# Prints Garbage collector as 0 object
print("Garbage collector: collected","%d objects." % collected)

#TELUSKO

a=10
b=a
print(id(a))#140732463896512
print(id(b))#140732463896512
print(id(10))#140732463896512
a=9
print(id(a))#140732463896480
b=a
print(id(b))#140732463896480

#Now 10 above is ready for garbage collection. 10 is called Object(data)