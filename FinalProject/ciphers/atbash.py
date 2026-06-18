def _get_alphabet(language):
    if language == 'ru':
        return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    else:
        return 'abcdefghijklmnopqrstuvwxyz'


def _reverse_char(ch, alphabet):
    if ch in alphabet:
        idx = alphabet.index(ch)
        return alphabet[len(alphabet) - 1 - idx]  # == alphabet[-idx]
    elif ch in alphabet.upper():
        idx = alphabet.upper().index(ch)
        return alphabet.upper()[len(alphabet) - 1 - idx]
    else:
        return ch


def encode(text, key=None, language='en'):
    alphabet = _get_alphabet(language)
    return ''.join(_reverse_char(ch, alphabet) for ch in text)


def decode(text, key=None, language='en'):
    encode(text, key, language)
