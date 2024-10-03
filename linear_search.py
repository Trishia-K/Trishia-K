#LINEAR SEARCH
def linear_search(array,target):
    for i in range(len(array)):#for every element in the of the range in the array
        if array[i]==target:
            return i
    return -1 
#Initialize dataset
data=[2,5,9,1,2]
target=9
#calling linear search function with its two variables, it's how we look for 9 in the array
result=linear_search(data, target)

if result!= -1:
    print("The element is at index",result)
else:
    print("Element not found")


#BINARY SEARCH
def binary_search(array1, target1):
    left=0
    right=len(array1)-1
    while left<=right:
        mid=(left+right)//2 #// returns a rounded off decimal

        if array1[mid]==target1:
            return mid
        elif array1[mid]<target1:
            left=mid+1
        else:
            right=mid-1
    return -1

array1=[1,3,5,7,9,10]
target1=7
result1=binary_search(array1,target1)

if result1 != -1:
    print("Element is at index",result1)
else:
    print("Element not found")

#LINEAR SEARCH MODIFIED-FIRST OCCURENCE

#BINARY SEARCH MODIFIED
    