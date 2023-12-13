# String Manipulation , guess and check, approximation and bisection

# Strings
""" 
1. think of as a sequence of case sensitive characters
2. can compare strings with ==, >, < etc.
3. len() is a function used to retrieve the length of the string in the parentheses
    s = "abc"
    len(s) -> evaluates to 3
4. square brackets used to perform indexing into a string to get the value at a certain index/position
    s = "abc"
    s[0] -> evaluates to "a"
    s[1] -> evaluates to "b"
    s[2] -> evaluates to "c"
    s[3] -> trying to index out of bounds, error
    s[-1] -> evaluates to "c"
    s[-2] -> evaluates to "b"
    s[-3] -> evaluates to "a"
5. can slice strings using [start:stop:step]
6. if give two numbers, [start:stop], step=1 by default
7. you can also omit numbers and leave just colons

    s = "abcdefgh"
    s[3:6] -> evaluates to "def", same as s[3:6:1]
    s[3:6:2] -> evaluates to "df"
    s[::] -> evaluates to "abcdefgh", same as s[0:len(s):1]
    s[::-1] -> evaluates to "hgfedbca", same as s[-1:-(len(s)+1):-1]
    s[4:1:-2]-> evaluates to "ec"
8. strings are “immutable” – cannot be modified
    s = "hello"
    s[0] = 'y' -> gives an error
    s = 'y'+s[1:len(s)] -> is allowed,s bound to new object
"""
# for LOOPS RECAP

""" 
1. for loops have a loop variable that iterates over a set of values
    for var in range(4): -> var iterates over values 0,1,2,3
    <expressions> -> expressions inside loop executed with each value for var
for var in range(4,6): -> var iterates over values 4,5
    <expressions>
2. range is a way to iterate over numbers, but a for loop variable can iterate over any set of values, not just numbers! 
"""
# STRINGS AND LOOPS
""" 
1. these two code snippets do the same thing
2. bottom one is more “pythonic”
s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")
for char in s:
    if char == 'i' or char == 'u':
    print("There is an i or u") 
"""
#  GUESS-AND-CHECK
""" 
1. the process below also called exhaustive enumeration
2. given a problem…
3. you are able to guess a value for solution
4. you are able to check if the solution is correct
5. keep guessing until find solution or guessed all values 
"""
# GUESS-AND-CHECK – cube root
""" cube = 8
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess) """
# GUESS-AND-CHECK – cube root
""" cube = 8
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
print('Cube root of '+str(cube)+' is '+str(guess)) """
# APPROXIMATE SOLUTIONS
""" 1. good enough solution
2. start with a guess and increment by some small value
3. keep guessing if |guess3-cube| >= epsilon for some small epsilon
4. decreasing increment size  slower program
5. increasing epsilon  less accurate answer """

# APPROXIMATE SOLUTION – cube root

""" cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube) """

# BISECTION SEARCH

""" 1. half interval each iteration
2. new guess is halfway in between
3. to illustrate, let's play a game! """

# BISECTION SEARCH – cube root

""" cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print ('num_guesses =', num_guesses)
print (guess, 'is close to the cube root of', cube) """

# BISECTION SEARCH CONVERGENCE

""" 1. search space
    => first guess: N/2
    => second guess: N/4
    => kth guess: N/2k
2. guess converges on the order of log2N steps
3. bisection search works when value of function varies
monotonically with input
4. code as shown only works for positive cubes > 1 – why?
5. challenges   -> modify to work with negative cubes!
                -> modify to work with x < 1! """

# x < 1

""" 
1. if x < 1, search space is 0 to x but cube root is greater than x and less than 1
2. modify the code to choose the search space
depending on value of x 
"""