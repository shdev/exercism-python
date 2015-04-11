roman_digits = [
    {
        1: 'I',
        5: 'V',
    },
    {
        1: 'X',
        5: 'L',
    },
    {
        1: 'C',
        5: 'D',
    },
    {
        1: 'M',
    }
]


def numeral(arabic):
    if arabic < 1:
        raise ValueError('Romans don\'t like numbers smaller than one')
    if arabic > 3000:
        raise ValueError('Romans don\'t like numbers bigger than'
                         ' three tausend')

    arabic = list(reversed(str(arabic)))
    roman = ''

    for i in range(len(arabic) - 1, - 1, - 1):
        if arabic[i] in ['1', '2', '3']:
            roman += roman_digits[i][1] * int(arabic[i])
        elif arabic[i] == '4':
            roman += roman_digits[i][1] + roman_digits[i][5]
        elif arabic[i] in ['5', '6', '7', '8']:
            roman += roman_digits[i][5] \
                + roman_digits[i][1] * (int(arabic[i]) - 5)
        elif arabic[i] == '9':
            roman += roman_digits[i][1] + roman_digits[i + 1][1]
    return roman
