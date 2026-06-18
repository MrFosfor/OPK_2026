from colorama import Fore, init

init(autoreset=True)


def _prepare_key_en(key):
    key = key.upper().replace("J", "I")
    seen = set()
    result = []
    for ch in key:
        if 'A' <= ch <= 'Z' and ch not in seen:
            seen.add(ch)
            result.append(ch)
    for code in range(ord('A'), ord('Z') + 1):
        ch = chr(code)
        if ch == "J":
            continue
        if ch not in seen:
            result.append(ch)
    return ''.join(result)


def _prepare_key_ru(key):
    key = key.upper().replace("Ё", "Е")
    seen = set()
    result = []
    for ch in key:
        if 'А' <= ch <= 'Я' and ch not in seen:
            seen.add(ch)
            result.append(ch)
    for code in range(ord('А'), ord('Я') + 1):
        ch = chr(code)
        if ch not in seen:
            result.append(ch)
    return ''.join(result) + ',' + '.' + '-'


def _prepare_text_en(text):
    text = ''.join(ch for ch in text.upper() if 'A' <= ch <= 'Z')
    text = text.replace('J', 'I')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                pairs.append(a + 'X')
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + 'X')
            i += 1
    return pairs


def _prepare_text_ru(text):
    text = ''.join(ch for ch in text.upper() if ('А' <= ch <= 'Я') or ch in (',', '.', '-'))
    text = text.replace('Ё', 'Е')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                pairs.append(a + 'Ъ')
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + 'Ъ')
            i += 1
    return pairs


def _process_pair(a, b, table, mode, language):
    num = 5 if language == 'en' else 6
    r1, c1 = _find_position(table, a, language)
    r2, c2 = _find_position(table, b, language)
    if r1 == r2:
        if mode == "encode":
            c1 = (c1 + 1) % num
            c2 = (c2 + 1) % num
        else:
            c1 = (c1 - 1) % num
            c2 = (c2 - 1) % num
    elif c1 == c2:
        if mode == "encode":
            r1 = (r1 + 1) % num
            r2 = (r2 + 1) % num
        else:
            r1 = (r1 - 1) % num
            r2 = (r2 - 1) % num
    else:
        c1, c2 = c2, c1
    return table[r1][c1] + table[r2][c2]


def _build_table(key, language):
    if language == "en":
        prepared = _prepare_key_en(key)
        return [list(prepared[i * 5:(i + 1) * 5]) for i in range(5)]
    else:
        prepared = _prepare_key_ru(key)
        return [list(prepared[i * 6:(i + 1) * 6]) for i in range(6)]


def _find_position(table, ch, language):
    num = 5 if language == 'en' else 6
    for i in range(num):
        for j in range(num):
            if table[i][j] == ch:
                return i, j
    return None


def encode(text, key, language='en'):
    table = _build_table(key, language)
    if language == 'en':
        pairs = _prepare_text_en(text)
    else:
        pairs = _prepare_text_ru(text)
    return ''.join(_process_pair(a, b, table, 'encode', language) for a, b in pairs)


def decode(text, key, language='en'):
    table = _build_table(key, language)
    if language == 'en':
        text = ''.join(ch for ch in text.upper() if 'A' <= ch <= 'z')
    else:
        text = ''.join(ch for ch in text.upper() if 'А' <= ch <= 'Я')
    if len(text) % 2 != 0:
        raise ValueError(Fore.LIGHTRED_EX + "Зашифрованный текст должен иметь четную длину.")
    pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
    return ''.join(_process_pair(a, b, table, 'decode', language) for a, b in pairs)
