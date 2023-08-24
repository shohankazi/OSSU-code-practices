# Finding the largest value

""" largest = 0
print('Before',largest)
for num in [9,41,12,3,74,15] :
    if num > largest :
        largest = num
    print(largest,num)
print('After',largest)
"""

# Counting in a loop
"""
zork = 0
print('Before',zork)
for thing in [9,41,12,3,74,15] :
    # print(thing)
    zork = zork + thing
    print(thing, " + ",zork)
print('After',zork)
"""

# Finding the average in a loop

"""
count = 0
sum = 0
print('Before',count,sum)
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    average = sum / count
    print(count,sum,value)
print('After',count,sum,average)
"""

# Filtering in a loop

""" print('Before')
for value in [9,41,12,3,74,15] :
    if value > 20 :
        print('Large number',value)
print('After') """

# Search Using a Boolean Variable

""" found = False
print('Before', found)
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True
    else :
        found = False
    print(found,value)
print('After',found) """

# Finding the smallest value

""" smallest = None
print('Before')
for value in [9,41,12,3,74,15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest,value)
print('After',smallest) """

# Write a program which repeatedly reads numbers until the users enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number

""" num = 0
total = 0.0
while True :
    string_value = input('Enter a number: ')
    if string_value == 'done' :
        break
    try:
        float_value = float(string_value)
    except:
        print("Invalid Input")
        continue
    num = num + 1
    total = total + float_value
print(total,num, total/num)
"""
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
""" largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        int_num = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or largest < int_num:
        largest = int_num
    if smallest is None or smallest > int_num:
        smallest = int_num
print("Maximum is", largest)
print("Minimum is", smallest) """

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')