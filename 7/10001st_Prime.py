def next_prime(primes):
    largest = primes[-1]
    while(True):
        largest += 2
        if is_divisible(largest, primes) == False:
            primes.append(largest)
            return primes

def is_divisible(n, facs):
    for fac in facs:
        if n % fac == 0:
            return True
    return False

def nth_prime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    primes = [3]
    for i in range(2, n):
        primes = next_prime(primes)
    return primes[-1]

print(nth_prime(21569))

