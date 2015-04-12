def sieve(n):
    # Simulate a bit array; each entry in [0, n] represents whether or not
    # the number at that index is prime.
    bitarray = [0] * (n + 1)
    # Follow the algorithm for the Sieve of Eratosthenes (starting with the
    # first prime, 2)...
    prime = 2
    while prime < n:
        # 1. Take the next available unmarked number in your list (it is prime)
        if bitarray[prime] == 0:
            i = 2
            # 2. Mark all the multiples of that number (they are not prime)
            while prime * i <= n:
                bitarray[prime * i] = 1
                i += 1
        prime += 1
    # Reduce the results (ignoring 0 and 1). Return the index of all entries
    # that have not yet been touched.
    return [idx for idx, p in enumerate(bitarray) if idx > 1 and p == 0]


def prime_factors(n):
    primes = sieve(n)
    prime_factors = []
    while primes:
        p = primes[0]
        if not n % p:
            prime_factors.append(p)
            n /= p
        else:
            del primes[0]

    return prime_factors
