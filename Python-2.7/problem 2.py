def fibonacciGenerator(max):
    first = 1
    second = 2
    fibonacci.append(first)
    fibonacci.append(second)
    while True:
        first = first + second
        if first <= max:
            fibonacci.append(first)
        else:
            break
        second = second + first
        if second <= max:
            fibonacci.append(second)
        else:
            break
    return fibonacci
	
fibonacci = []	
total = 0
max = 4000000

fibonacci = fibonacciGenerator(max)

for y in fibonacci:
    if y % 2 == 0:
        total = total + y
print total

fibonacci = []
fibonacci = fibonacciGenerator(max)

print sum(filter(lambda x: x % 2 == 0, fibonacci))
