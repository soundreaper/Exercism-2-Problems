def prime(number):
    if number == 0:
        raise ValueError("There is no 0th prime!")
    primes = []
    current = 2
    while len(primes) < number:
        if not is_divisible(current, primes):
            primes.append(current)
        current += 1
    return primes[-1]

def is_divisible(current, primes):
    return any(current % p == 0 for p in primes if current >= p ** 2)