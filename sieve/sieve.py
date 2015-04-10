def sieve(n):
    candidates = range(2, n + 1)
    primes = []
    while candidates:
        prime = candidates[0]
        del candidates[0]
        primes += [prime]
        candidates = [c for c in candidates if c % prime]

    return primes
