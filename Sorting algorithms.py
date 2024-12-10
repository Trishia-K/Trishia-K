#Bubble sort(O(n2))
array=[12,9,10,14,5,3,6]
n=len(array)
for i in range(n-1):
    for j in range (n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print("Sorted array= ",array)

#Selection sort(O(n2))
my_array = [15,13,7,19,3,4,10,1]
n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)
print("Sorted array:", my_array)

#Insertion Sort
myarray = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(myarray)
for i in range(1,n):
    insert_index = i
    current_value = myarray.pop(i)
    for j in range(i-1, -1, -1):
        if myarray[j] > current_value:
            insert_index = j
    myarray.insert(insert_index, current_value)

print("Sorted array:", myarray)

#Quick sort
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

#Merge sort(The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking
#it down into smaller arrays, and then building the array back together the correct way so that it is sorted.)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

#Linear search
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

#Binary search
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


#Implementation of a Stack
stack = []
# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)
# Pop
element = stack.pop()
print("Pop: ", element)
# Peek
topElement = stack[-1]
print("Peek: ", topElement)
# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)
# Size
print("Size: ",len(stack))

#Implementing a queue
queue = []
# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)
# Dequeue
element = queue.pop(0)
print("Dequeue: ", element)
# Peek
frontElement = queue[0]
print("Peek: ", frontElement)
# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)
# Size
print("Size: ", len(queue))


#Binary Search Tree Implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)

#Implementation of Dijkstra Algorithm
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data