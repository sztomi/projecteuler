from math import log, sqrt, floor, ceil

def isprime(x):
    if (x == 2): return True
    if (x % 2 == 0): return False
    high = int(floor(sqrt(x)))

    for d in xrange(3, high+1):
        if (x % d) == 0: 
            return False
            
    return True

def nthprime(N):
    print isprime(1)
    count, result = 0, 1
    while count < N:
        result += 1
        if isprime(result): count += 1

    return result


print nthprime(10001)

	

