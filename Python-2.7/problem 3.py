number = 600851475143

primes = []
pFactors = []

def SieveOfAtkin(limit):
    results = [2, 3, 5]
    sieve = [i for i in xrange(limit + 1)]
    TF = [False] * (limit + 1)
    ModFour = [1, 13, 17, 29, 37, 41, 49, 53]
    ModSix = [7, 19, 31, 43]
    ModTwelve = [11, 23, 47, 59]

    for x in xrange(1, int((limit ** 0.5)) + 1):
        for y in xrange(1, int((limit ** 0.5)) + 1):
            test = 4 * x**2 + y**2 
            if test % 60 in ModFour:
                try:
                    TF[test] = not TF[test]
                except IndexError:
                    pass 
            test = 3 * x**2 + y**2
            if test % 60 in ModSix:
                try:
                    TF[test] = not TF[test]
                except IndexError:
                    pass 
            if x > y:
                test = 3 * x**2 - y**2
                if test % 60 in ModTwelve:
                    try:
                        TF[test] = not TF[test]
                    except IndexError:
                        pass 
    for n in xrange(5, int((limit ** 0.5))):
        if TF[n] == True:
            for x in xrange((n**2), (limit + 1), (n**2)):
                TF[x] = False
    
    for p in xrange(5, limit + 1):
        if TF[p] == True:
            results.append(sieve[p])

    return results

def GetPrimeFactors(test, primes):
    Pfactors = []
    number = test

    for num in primes:
        if number < num:
            return Pfactors 
        while True:
            if number % num == 0:
                number = number / num
                Pfactors.append(num)
            else:
                break
            if number < num:
                break  
        if number == 1:
            return Pfactors
    print "reached end of for loop"
    return Pfactors 

primes = SieveOfAtkin(int(number ** 0.5))

pFactors = GetPrimeFactors(number, primes)
largest = 1
for x in pFactors:
    if x > largest:
        largest = x
print "The prime factors of", number, "are",
for x in pFactors:
    print x,
print 
print "The largest prime factor of", number, "is", largest
