def linear_search_modified(array,target):
    indices=[]

    for i in range(len(array)):
        if array[i]==target:
         indices.append(i)

    return indices
array=[1,4,6,7,9,4,4,4,5,4,5]
target=4
result=linear_search_modified(array,target)
if result:
   print("elemnts found at indices",result)
else:
   print("Element not found")   