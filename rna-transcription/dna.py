mapping = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna):
    return_string = ''

    for acid in dna:
        return_string += mapping[acid]

    return return_string
