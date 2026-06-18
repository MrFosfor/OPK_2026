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
    for symbol in (',', '.', '-', '/'):
        if symbol not in seen:
            result.append(symbol)
    return ''.join(result)


def _prepare_text(text, language):
    if language == 'en':
        text = ''.join(ch for ch in text.upper() if 'A' <= ch <= 'Z')
        text = text.replace('J', 'I')
        symbol = 'X'
    else:
        text = ''.join(ch for ch in text.upper().replace('Ё', 'Е') if ('А' <= ch <= 'Я') or ch in (',', '.', '-', '/'))
        symbol = 'Ъ'
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                pairs.append(a + symbol)
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + symbol)
            i += 1
    return pairs


def _process_pair(a, b, table, mode, language):
    num = 5 if language == 'en' else 6
    pos1 = _find_position(table, a, language)
    pos2 = _find_position(table, b, language)
    if pos1 is None or pos2 is None:
        raise ValueError("Символ отсутствует в таблице. Попробуйте снова")
    else:
        r1, c1 = pos1
        r2, c2 = pos2
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


def _del_sep(text, language):
    symbol = 'X' if language == 'en' else 'Ъ'
    if len(text) <= 1:
        return text
    result = [text[0]]
    for i in range(1, len(text) - 1):
        ch = text[i]
        if ch == symbol and text[i - 1] == text[i + 1]:
            continue
        result.append(ch)
    if text[-1] != symbol:
        result.append(text[-1])
    return ''.join(result)


def encode(text, key, language='en'):
    table = _build_table(key, language)
    pairs = _prepare_text(text, language)
    return ''.join(_process_pair(a, b, table, 'encode', language) for a, b in pairs)


def decode(text, key, language='en'):
    table = _build_table(key, language)
    if language == 'en':
        text = ''.join(ch for ch in text.upper().replace('J', 'I') if 'A' <= ch <= 'Z')
    else:
        text = ''.join(ch for ch in text.upper().replace('Ё', 'Е') if 'А' <= ch <= 'Я' or ch in (',', '.', '-', '/'))
    if len(text) % 2 != 0:
        raise ValueError("Зашифрованный текст должен иметь четную длину.")
    pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
    return _del_sep(''.join(_process_pair(a, b, table, 'decode', language) for a, b in pairs), language)
