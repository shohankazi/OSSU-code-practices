# complexities
""" 
### Logarithmic Complexity (O(log n))

Logarithmic complexity is often considered an efficient algorithmic complexity class. In this class, the running time of an algorithm grows logarithmically with the input size. This means that as the input size (n) increases, the time taken by the algorithm increases, but at a much slower rate compared to linear or quadratic complexities.

A common example of an algorithm with logarithmic complexity is binary search. Binary search is used to find an item in a sorted list by repeatedly dividing the list in half until the target item is found. Here's a Python example:

Example: 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(my_list, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")


In the binary search example, each comparison reduces the search space in half. So, even if the list is very large, the number of iterations needed to find the target remains relatively small. This is a characteristic of algorithms with logarithmic complexity.

Next, we'll explore polynomial complexity.

==>Polynomial Complexity (O(n^k))

Polynomial complexity is characterized by algorithms where the running time grows as a polynomial of the input size (n). The highest power of the polynomial, represented by 'k,' determines the degree of the polynomial complexity.

An example of an algorithm with polynomial complexity is the bubble sort algorithm. Bubble sort compares adjacent elements in a list and swaps them if they are in the wrong order. This process is repeated until the entire list is sorted. Bubble sort has a worst-case time complexity of O(n^2) because it involves nested loops.

Here's a Python example of bubble sort:

Example:
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)
```

Bubble sort compares all pairs of elements in the list, which results in a quadratic growth in running time as the input size increases.

Lastly, we'll discuss exponential complexity.

===> Exponential Complexity (O(2^n))

Exponential complexity is the least efficient class of algorithms. In this class, the running time grows exponentially with the input size. This means that for each additional element in the input, the running time can double or more.

A classic example of an algorithm with exponential complexity is the recursive Fibonacci sequence calculator:

Example:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
result = fibonacci(6)
print("Fibonacci(6) =", result)


In this example, the Fibonacci sequence is calculated recursively. The number of recursive calls grows exponentially with 'n,' resulting in exponential time complexity.

Understanding these complexity classes is essential for analyzing and designing efficient algorithms. 
"""