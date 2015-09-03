numbers = 0
for x in range(1, 1000):
    if x % 3 == 0: numbers = numbers + x
    elif x % 5 == 0: numbers = numbers + x
print numbers



multiples = []
for x in range(0, 1000, 3):	multiples.append(x)
for y in range(0, 1000, 5):	multiples.append(y)
print sum(list(set(multiples)))
    


print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000)))
