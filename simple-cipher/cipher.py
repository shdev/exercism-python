from random import randint
from itertools import cycle


class ArgumentError(Exception):
    def __init__(self, value):
        super(ArgumentError, self).__init__()
        self.value = value

    def __repr__(self):
        return self.value


class Cipher(object):
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, key=None):
        super(Cipher, self).__init__()

        if key is None:
            key = self.generate_key(100)
        else:
            if not self.is_key_valid(key):
                raise ArgumentError('some charactor are not included in \'' +
                                    self._alphabet + '\'')

        self.key_as_ord = [ord(l) - ord('a') for l in key]

    def encode(self, text):
        text = self.sanitize_str(text.lower())
        return ''.join(self._encodechar(l, c)
                       for l, c in zip(text, cycle(self.key_as_ord)))

    def decode(self, text):
        return ''.join(self._decodechar(l, c)
                       for l, c in zip(text, cycle(self.key_as_ord)))

    @classmethod
    def _encodechar(cls, char, cipher):
        return chr(((ord(char) - ord('a') + cipher) %
                   (ord('z') - ord('a') + 1)) + ord('a'))

    def _decodechar(self, char, cipher):
        return chr(((ord(char) - ord('a') - cipher) %
                   (ord('z') - ord('a') + 1)) + ord('a'))

    def getkey(self):
        return ''.join(chr(o) for o in self.key_as_ord)

    @classmethod
    def generate_key(cls, length):
        return ''.join(chr(randint(97, 122)) for i in xrange(0, length))

    @classmethod
    def is_key_valid(cls, key):
        for l in key:
            if l not in cls._alphabet:
                return False

        return True

    @classmethod
    def sanitize_str(cls, text):
        return ''.join(l for l in text if l in cls._alphabet)


class Caesar(Cipher):

    def __init__(self):
        super(Caesar, self).__init__('d')

        
