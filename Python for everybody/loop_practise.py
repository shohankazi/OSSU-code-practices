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

smallest = None
print('Before')
for value in [9,41,12,3,74,15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest,value)
print('After',smallest)