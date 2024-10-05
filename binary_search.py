def binary_search(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2

        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

array=[1,3,5,7,9,10]        
target=7
result=binary_search(array,target)

if result!= -1:
    print("Element is at index",result)
else:
    print("Element not found")    
