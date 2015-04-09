mapping = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna):
    return_string = ''

    for i in xrange(0, len(dna)):
        return_string += mapping[dna[i]]

    return return_string
