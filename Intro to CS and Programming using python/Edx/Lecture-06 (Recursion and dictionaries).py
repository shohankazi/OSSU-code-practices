# RECURSION
# Recursion is the process of repeating items in a self-similar way

# WHAT IS RECURSION?
""" 1. Algorithmically:	a way to design	solutions to problems by divide-and-conquer	or decrease-and-conquer         
    => reduce a problem to simpler versions of the same problem		
2. Semantically: a programming technique where a function calls itself
	=> in programming, goal	is to NOT have infinite	recursion
    => 	must have 1	or more	base cases that	are	easy to	solve
    => must	solve the same problem on some other input with	the	goal of	simplifying	the	larger problem input	
"""
# ITERATIVE ALGORITHMS SO FAR
""" 
1. looping constructs (while and for loops)	lead to	iterative algorithms
2. can capture computation in a	set	of state variables that	update on each iteration through loop 
"""
# SOME OBSERVATIONS
""" 
1. each	recursive call to a	function creates its own scope/environment	
2. bindings	of variables in	a scope	are	not	changed	by	recursive call	
3. flow	of control passes back to previous scope once function call	returns	value 
"""
# ITERATION vs. RECURSION
# iterative way
""" 
def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod
"""
# Recursive way
""" 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
"""
""" 
1. recursion may be	simpler, more intuitive	
2. recursion may be	efficient from programmer POV
3. recursion may not be	efficient from computer	POV
"""
# DIVIDE AND CONQUER
""" 
1. an example of a “divide and conquer”	algorithm	
2. solve a hard	problem	by breaking	it into	a set of sub-problems such that:	
    ◦ sub-problems are easier to solve than	the	original	
    ◦ solutions of the sub-problems can be combined to solve the original
"""
# DICTIONARIES
""" 
1. a separate list for each item
2. each	list must have the same length
3. info	stored across lists	at same	index, each	index refers to	info for a different person 
"""
# HOW TO UPDATE/RETRIEVE STUDENT INFO
""" 
1. messy if	have a lot of different	info to	keep track of
2. must	maintain many lists and	pass them as arguments
3. must	always index using integers
4. must	remember to	change multiple lists
"""
""" 
DICTIONARY KEYS and VALUES

1.	values		
    • 	any	type	(immutable	and	mutable)	
    • 	can	be	duplicates	
    • 	dictionary	values	can	be	lists,	even	other	dictionaries!
2.	keys	
    • 	must	be	unique		
    • 	immutable	type	(int,	float,	string,	tuple,bool)	
    •   actually	need	an	object	that	is	hashable,	but	think	of	as	immutable	as	all	immutable	types	are	hashable	
    • 	careful	with	float	type	as	a	key	
3.  no	order	to	keys	or	values!	
d = {4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44]} 
"""
# MEMOIZATION
""" 
Memoization is a technique in Python (and in computer science in general) used to optimize the performance of functions by caching, or storing, the results of expensive function calls so that they can be quickly retrieved when needed again. In simple terms, it's like creating a memory or memo for a function to remember its previous calculations.

Here's a basic explanation with an industry-level example:

**Scenario: Calculating Fibonacci Numbers**

Imagine you're building a software program that needs to calculate Fibonacci numbers. Fibonacci numbers are a sequence where each number is the sum of the two preceding ones, like this: 0, 1, 1, 2, 3, 5, 8, 13, and so on.

**Without Memoization:**

If you calculate Fibonacci numbers without memoization, you might end up recalculating the same values multiple times. For example, to find the 5th Fibonacci number, you'd need to calculate the 4th and 3rd Fibonacci numbers, and to calculate the 4th Fibonacci number, you'd need to calculate the 3rd and 2nd Fibonacci numbers. As you can see, there's a lot of redundancy in these calculations.

**With Memoization:**

Now, let's introduce memoization. Instead of recalculating Fibonacci numbers each time, you store the results of previous calculations in a memory (like a dictionary in Python) so that you can reuse them later. Here's how it works:

1. You start by defining a memoization container (e.g., a dictionary) to store calculated Fibonacci numbers.

2. When you need to calculate a Fibonacci number, you first check if it's already in the memoization container.

3. If it's there, you simply return the stored result. If not, you calculate it and store it in the container for future use.

Here's a Python example using memoization to calculate Fibonacci numbers:

```python
# Memoization container (dictionary)
fib = int(input("enter a number "))
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    
    fib_cache[n] = result
    return result

print(fibonacci(fib))

# Usage
print(fibonacci(5))  # This will efficiently calculate and print the 5th Fibonacci number.
```

With memoization, the function stores the results of previously calculated Fibonacci numbers, making it much faster and more efficient, especially for large Fibonacci numbers. This technique is widely used in industry-level applications to optimize functions that involve repetitive calculations.
"""

