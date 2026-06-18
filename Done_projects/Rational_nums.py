class Rational:
    pass


def add(a, b):  # Проверка сделана
    c = Rational()
    if a.d == b.d:
        c.n = a.n + b.n
        c.d = b.d
    else:
        c.n = a.n * b.d + b.n * a.d
        c.d = a.d * b.d

    c = to_canonical(c)

    return c


def sub(a, b):  # Проверка сделана
    c = Rational()
    if a.d == b.d:
        c.n = a.n - b.n
        c.d = b.d
    else:
        c.n = a.n * b.d - b.n * a.d
        c.d = a.d * b.d

    c = to_canonical(c)

    return c


def mul(a, b):  # Проверка сделана
    c = Rational()
    c.n = a.n * b.n
    c.d = a.d * b.d

    c = to_canonical(c)

    return c


def div(a, b):  # Проверка сделана
    c = Rational()
    if a.n == 0 or b.n == 0:
        raise ZeroDivisionError
    else:
        c.n, c.d = b.d, b.n

    return mul(a, c)


def power(a, p):  # Проверка сделана
    c = Rational()
    if p < 0:
        p = -p
        if a.n == 0:
            raise ZeroDivisionError
        c.n, c.d = a.d, a.n
    elif p == 0:
        c.n, c.d = 1, 1
    else:
        c.n, c.d = a.n, a.d

    c.n **= p
    c.d **= p

    c = to_canonical(c)

    return c


def create(numer, denom):  # Проверка сделана
    if denom == 0:
        raise ZeroDivisionError
    else:
        r = Rational()
        if numer < 0 < denom or numer > 0 > denom:
            numer = -abs(numer)
            denom = abs(denom)
        else:
            numer = abs(numer)
            denom = abs(denom)

        r.n = numer
        r.d = denom

        r = to_canonical(r)

        return r


def compare(a, b):  # Проверка сделана
    if a.n * b.d == b.n * a.d:
        return 0
    elif a.n * b.d > b.n * a.d:
        return 1
    else:
        return -1


def to_int(r):  # Проверка сделана
    return r.n // r.d


def to_float(r):  # Проверка сделана
    return r.n / r.d


def to_str(r):  # Проверка сделана
    if r.d == 1:
        temp = str(r.n)
    else:
        temp = str(r.n) + "/" + str(r.d)

    return temp


def nod(num, dem):  # Проверка сделана
    max_nod = 1
    for i in range(2, min(num, dem) + 1):
        if num % i == 0 and dem % i == 0:
            max_nod = i
    return max_nod


def to_canonical(r):  # Проверка сделана
    answer = Rational()
    num = r.n
    den = r.d

    if abs(num) // den == abs(num) / den:
        answer.n = num // den
        answer.d = 1
    else:
        temp = nod(num, den)
        answer.n = num // temp
        answer.d = den // temp

    return answer
