"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

##Version 1##
numbers = 0
for x in range(1, 1000):
    if x % 3 == 0: numbers = numbers + x
    elif x % 5 == 0: numbers = numbers + x
        
print numbers


##Version 2##
multiples = []

for x in range(0, 1000, 3):	multiples.append(x)
for y in range(0, 1000, 5):	multiples.append(y)
print sum(list(set(multiples)))
    

##Version 3##
print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000)))
