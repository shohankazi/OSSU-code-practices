# Finding the largest value
"""
largest = 0
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

count = 0
sum = 0
print('Before',count,sum)
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    print(count,sum,value)
print('After',count,sum,sum/count)