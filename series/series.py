def slices(number_list, slice_size):
    if slice_size > len(number_list) or slice_size < 1:
        raise ValueError

    number_list = [int(c) for c in number_list]

    return [number_list[i:i + slice_size]
            for i in xrange(0, len(number_list) + 1 - slice_size)]
