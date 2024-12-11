# (a) Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

# Operations on Stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.display())

stack.pop()
stack.pop()

print("Stack after popping two elements:", stack.display())

# (b) Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue
    # Operations on Queue
queue = Queue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")
queue.enqueue("Diana")
queue.enqueue("Eve")

print("Queue after enqueues:", queue.display())

queue.dequeue()
queue.dequeue()

print("Queue after dequeuing two elements:", queue.display())


# (a) Sum of the first n natural numbers

def sum_of_natural_numbers(n):
    """
    Calculate the sum of the first n natural numbers.
    :param n: int, the number of natural numbers to sum
    :return: int, the sum of the first n natural numbers
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Time complexity: O(n)
# Space complexity: O(1)

# Example usage:
n = 10
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers(n)}")

# (b) Binary search implementation
def binary_search(arr, target):
    """
    Perform a binary search on a sorted array.
    :param arr: list of sorted integers
    :param target: int, the number to search for
        :return: int, the index of the target if found, else -1
    """
    left, right = 0, len(arr) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"Number of comparisons: {comparisons}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Number of comparisons: {comparisons}")
    return -1
# Time complexity: O(log n)
# Space complexity: O(1)

# Example usage:
sorted_array = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = binary_search(sorted_array, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the array.")



# (a) Insertion Sort Implementation
def insertion_sort(arr):
    """
    Perform insertion sort and display the array after each pass.
    :param arr: list of integers to be sorted
    :return: None
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        # Display array after each pass
        print(f"Pass {i}: {arr}")

# Example usage
unsorted_array = [34, 8, 64, 51, 32, 21, 87, 43, 76, 19]
print("Initial array:", unsorted_array)
insertion_sort(unsorted_array)
print("Sorted array:", unsorted_array)
# (b) Bubble Sort Implementation
def bubble_sort(arr):
    """
    Perform bubble sort and count the number of swaps made.
    :param arr: list of integers to be sorted
    :return: int, the number of swaps made
    """
    n = len(arr)
    swap_count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

    return swap_count
# Example usage
unsorted_array_bubble = [64, 34, 25, 12, 22, 11, 90]
print("Initial array:", unsorted_array_bubble)
swaps = bubble_sort(unsorted_array_bubble)
print("Sorted array:", unsorted_array_bubble)
print(f"Total number of swaps: {swaps}")
