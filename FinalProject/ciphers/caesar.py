def _get_alphabet(language):
    if language == 'ru':
        return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    else:
        return 'abcdefghijklmnopqrstuvwxyz'

def _shift_char(ch, shift, alphabet):
    if not isinstance(shift, int):
        raise TypeError('Сдвиг должен быть целым числом.')
    if ch in alphabet:
        idx = alphabet.index(ch)
        new_idx = (idx + shift) % len(alphabet)
        return alphabet[new_idx]
    elif ch in alphabet.upper():
        idx = alphabet.upper().index(ch)
        new_idx = (idx + shift) % len(alphabet)
        return alphabet.upper()[new_idx]
    else:
        return ch

def encode(text, shift, language='en'):
    alphabet = _get_alphabet(language)
    return ''.join(_shift_char(ch, shift, alphabet) for ch in text)

def decode(text, shift, language='en'):
    return encode(text, -shift, language)
