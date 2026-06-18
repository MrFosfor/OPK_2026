def _get_alphabet(language):
    if language == 'ru':
        return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    else:
        return 'abcdefghijklmnopqrstuvwxyz'


def _hash(key, pos):
    s = key + str(pos)
    h = 0
    for ch in s:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return h


def _shift_char(ch, shift, alphabet, direction):
    if ch in alphabet:
        idx = alphabet.index(ch)
        return alphabet[(idx + shift * direction) % len(alphabet)]
    elif ch in alphabet.upper():
        idx = alphabet.upper().index(ch)
        return alphabet.upper()[(idx + shift * direction) % len(alphabet)]
    else:
        return ch


def encode(text, key, language='en'):
    alphabet = _get_alphabet(language)
    res = []
    for i, ch in enumerate(text):
        shift = _hash(key, i) % len(alphabet)
        res.append(_shift_char(ch, shift, alphabet, 1))
    return ''.join(res)


def decode(text, key, language='en'):
    alphabet = _get_alphabet(language)
    res = []
    for i, ch in enumerate(text):
        shift = _hash(key, i) % len(alphabet)
        res.append(_shift_char(ch, shift, alphabet, -1))
    return ''.join(res)
