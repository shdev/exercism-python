import operator


def slices(number_list, slice_size):
    if slice_size > len(number_list) or slice_size < 1:
        raise ValueError

    number_list = [int(c) for c in number_list]

    return [number_list[i:i + slice_size]
            for i in xrange(0, len(number_list) + 1 - slice_size)]


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def largest_product(number_list, slice_size):
    if slice_size == 0:
        return 1

    slice_list = slices(number_list, slice_size)

    products = [prod(slice) for slice in slice_list]

    return max(products)
