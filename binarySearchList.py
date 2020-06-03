#binarySearch with List using for loop
#For binarySearch values should be sorted fist else it will not work

print('********BinarySearch with List using for loop****')
pos =-1#Counter
def search(list1,n):
    l=0
    u=len(list1)-1

    while l<=u:
        mid = (l+u)//2

        if list1[mid]==n:
            global pos
            pos=mid
            return True
        else:
            if list1[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False #This is inside While

list = [4,7,8,12,45,99,102,702,10997,56666]

#Search 102
n=102

if search(list,n):
    print('found at ',pos+1)
else:
    print('Not found at ')