""" 
1. **Linear Search**:
   - **Description**: Linear search is a simple searching algorithm that checks each element in a list or array one by one until a match is found or the entire list is searched.
   - **Example**: Imagine you have a list of customer names and you want to find a specific customer by their name in a database. You would start from the beginning and check each name until you find the one you're looking for.

2. **Monkey Sort** (also known as Bogosort):
   - **Description**: Monkey sort is a highly inefficient sorting algorithm that shuffles the elements randomly until they happen to be in the correct order.
   - **Example**: Think of a scenario where you have a deck of cards, and you want to arrange them in ascending order. With monkey sort, you would shuffle the deck repeatedly until, by pure chance, the cards end up sorted.

3. **Bisection Search** (Binary Search):
   - **Description**: Bisection search is an efficient search algorithm for sorted lists or arrays. It repeatedly divides the list in half and narrows down the search space.
   - **Example**: Suppose you have a sorted list of numbers, and you want to find a specific number. You would start by checking the middle element. If the target is greater than the middle, you'd discard the left half; if it's smaller, you'd discard the right half. Repeat this process until you find the target or determine it's not in the list.

4. **Bubble Sort**:
   - **Description**: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - **Example**: Imagine you have a list of exam scores, and you want to arrange them in ascending order. Bubble sort would compare each pair of adjacent scores and swap them if they are out of order, repeating this process until no more swaps are needed.

5. **Selection Sort**:
   - **Description**: Selection sort is another simple sorting algorithm that repeatedly selects the minimum (or maximum) element from the unsorted part of the list and moves it to the sorted part.
   - **Example**: If you have an array of student grades and you want to arrange them in ascending order, selection sort would repeatedly find the lowest grade and place it at the beginning of the sorted portion, working its way through the array.

6. **Loop Invariant**:
   - **Description**: A loop invariant is a property or condition that holds true before and after each iteration of a loop. It helps ensure the correctness of algorithms.
   - **Example**: When using a loop to search or sort data, a loop invariant might be that the smallest number in an unsorted portion of an array is correctly identified and placed in the sorted portion after each iteration.

7. **Merge Sort**:
   - **Description**: Merge sort is an efficient, comparison-based sorting algorithm that divides the input list into smaller sublists, sorts them, and then merges them back together.
   - **Example**: In a large dataset of customer records, merge sort could be used to sort the records by last name. It would divide the dataset into smaller chunks, sort them individually by last name, and then merge them into a fully sorted list.

These algorithms are fundamental to computer science and can be applied in various industry scenarios, from data analysis to software development and beyond. Understanding them will provide you with a strong foundation in computer science and algorithms.
"""
# code examples : 
""" 
1. **Linear Search**:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found the target
    return -1  # Target not found

# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_value = 6
result = linear_search(my_list, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found")
```

2. **Bisection Search (Binary Search)**:

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage (assuming the list is sorted)
my_sorted_list = [1, 3, 5, 6, 9, 12, 17, 22]
target_value = 9
result = binary_search(my_sorted_list, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found")
```

3. **Bubble Sort**:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array using Bubble Sort:", my_list)
```

4. **Selection Sort**:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Sorted array using Selection Sort:", my_list)
```

5. **Merge Sort**:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
merge_sort(my_list)
print("Sorted array using Merge Sort:", my_list)
```
"""
# Bogosort Algorithm
""" 
BogoSort is a highly inefficient and humorous sorting algorithm. It randomly shuffles the elements of an array repeatedly until it happens to be in sorted order. Here's a Python example of BogoSort:

```python
import random

def is_sorted(arr):
    # Check if the array is sorted
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", my_list)

bogosort(my_list)
print("Sorted array using BogoSort (may take a long time or forever):", my_list)
```

Keep in mind that BogoSort is not suitable for practical use and is used mostly for educational or humorous purposes. It has an average-case time complexity of O((n+1)!), making it extremely inefficient.
"""