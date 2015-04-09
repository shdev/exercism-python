def distance(str1, str2):
    return sum(1 for (elem1, elem2) in zip(str1, str2) if elem1 != elem2)
