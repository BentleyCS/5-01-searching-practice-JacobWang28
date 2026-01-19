import random


def randomSearch(items:list, target) -> int:
    tries=0
    while True:
        index=random.randint(0,len(items)-1)
        tries+=1
        if items[index]==target:
            print("number of tries=", tries)
            return index
list=[1,2,3,4,5]
print(randomSearch(list,4))

    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value


def linearSearch(items:list, target) ->tuple[int,int]:
    checks=0
    for i in range(len(items)):
        checks+=1
        if items[i]==target:
            return i,checks
    return -1,checks
list=[3,4,5,6,9]
print(linearSearch(list,0))

    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.



def binarySearch(items:list, target) -> tuple[int,int]:
    left=0
    right=len(items)-1
    checks=0
    while left<=right:
        checks+=1
        mid=(left+right)//2
        if items[mid]==target:
            return mid,checks
        elif items[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1, checks
list=[1,3,4,6,5,7]
print(binarySearch(list,6))
    # Modify the below function such that it implements binary search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.

