from math import ceil, sqrt
from string import punctuation, whitespace


def encode(text):
    text = ''.join(l for l in text.upper()
                   if l not in punctuation + whitespace)

    if not text:
        return ''
    column_count = int(ceil(sqrt(len(text))))

    lines = [text[i:i + column_count]
             for i in range(0, len(text), column_count)]

    squared = []

    for line in lines:
        for c in xrange(0, column_count):
            squared[c] = 

    return ' '.join(lines)
