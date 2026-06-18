import Rational_nums as r


def test():
    n_1, n_2 = 4, 8
    n_3, n_4 = 6, 10
    assert r.nod(n_1, n_2) == 4
    assert r.nod(n_3, n_4) == 2
    x_1 = r.to_canonical(r.create(8, 2))
    assert r.to_str(x_1) == "4"
    x_2 = r.to_canonical(r.create(6, 8))
    assert r.to_str(x_2) == "3/4"
    a = r.create(3, 2)  # 3/2
    assert r.to_int(a) == 1
    b = r.create(1, 2)  # 1/2
    assert r.to_float(b) == 0.5
    c = r.add(a, b)
    assert r.to_str(c) == "2"  # Вывод: "2"
    d = r.create(15, 1)
    assert r.to_str(d) == "15"
    e = r.sub(a, b)
    assert r.to_str(e) == "1"
    f = r.create(-2, -2)
    assert r.to_str(f) == "1"
    g = r.create(-2, 2)
    assert r.to_str(g) == "-1"
    h = r.create(2, 3)
    j = r.add(h, g)
    assert r.to_str(j) == "-1/3"
    i = r.mul(a, b)
    assert r.to_str(i) == "3/4"
    l = r.div(a, b)
    assert r.to_str(l) == "3"
    m_1 = r.power(b, 2)
    assert r.to_str(m_1) == "1/4"
    m_2 = r.power(b, -2)
    assert r.to_str(m_2) == "4"
    m_3 = r.power(b, 0)
    assert r.to_str(m_3) == "1"
    m_4 = r.power(i, -2)
    assert r.to_str(m_4) == "16/9"
    assert r.compare(a, b) == 1
    assert r.compare(b, b) == 0
    assert r.compare(b, a) == -1


if __name__ == '__main__':
    test()
