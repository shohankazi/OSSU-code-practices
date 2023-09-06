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