def sum_of_multiples(n, factors=[3, 5]):
    summands = []

    for i in xrange(1, n):
        isfactor = False
        for factor in factors:
            try:
                isfactor = isfactor or not i % factor
            except ZeroDivisionError:
                pass
        if isfactor:
            summands.append(i)

    return sum(summands)
