import string


def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(True for a in alphabet if a in s)


is_pangram('This is a really long text line.')


