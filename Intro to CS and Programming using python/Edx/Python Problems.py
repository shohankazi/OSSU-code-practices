# Problem 1
""" 
num = 10
for num in range(5):
    print(num)
print(num) 
"""

# Problem 2

""" divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) """ 

# Problem 3

""" for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') """

# Problem 4

""" for letter in 'hola':
    print(letter)   """

# Problem 5

""" count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count) """

# problem 6

""" myStr = '6.00x'

for char in myStr:
    print(char)

print('done') """

# Problem 7

""" greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done') """

# Problem 8

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))