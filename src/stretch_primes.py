def is_prime(num):
    if num == 1:
        return True
    elif num == 2:
        return True
    elif num == 3:
        return True
    else:
        for i in range(2, num, 1):
            if num % i == 0:
                return False
    return True

test = [1,2,3,4,5,6,7,8,9,10]

for t in test:
    print(f'{t} {"is prime" if is_prime(t) else "is not prime"}')


def sieve_of_eratosthenes(limit):
    primes = list(range(2,limit))
    for num in primes:
        print(num)
        primes = list(filter(lambda x: x % num != 0, primes))
    return primes

print(sieve_of_eratosthenes(10))

