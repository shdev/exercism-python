from string import maketrans, punctuation, whitespace

alphabet = 'abcdefghijklmnopqrstuvwxyz'
atbash_cipher_trans = maketrans(alphabet, alphabet[::-1])


def decode(text):
    text = ''.join(text.split())
    return text.translate(atbash_cipher_trans)


def encode(text):
    text = ''.join([l for l in text
                    if l not in punctuation and
                    l not in whitespace])
    text = text.lower()
    encoded = text.translate(atbash_cipher_trans)

    return insert_columns(encoded, 5)


def insert_columns(text, column_width):
    half_filled_column = 1 if len(text) % column_width else 0

    return ' '.join([text[i * column_width:(i + 1) * column_width]
                    for i in xrange(0, (len(text) / column_width)
                     + half_filled_column)])
