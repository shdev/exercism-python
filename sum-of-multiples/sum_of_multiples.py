def sum_of_multiples(n, factors=[3, 5]):
    summands = []

    if 0 in factors:
        factors.remove(0)

    for i in xrange(1, n):
        if any(not i % factor for factor in factors):
            summands.append(i)

    return sum(summands)
