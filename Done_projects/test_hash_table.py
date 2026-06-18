import hash_table as ht

def test_createHashTable():
    t = ht.createHashTable(hash)
    assert ht.size(t) == 0
    assert ht.isEmpty(t) is True
    assert t.capacity == 100
    assert t.alpha == 0.75
    t2 = ht.createHashTable(hash, initialCapacity=50)
    assert t2.capacity == 50
    def my_hash(x):
        return 42
    t3 = ht.createHashTable(my_hash)
    assert t3.hash(100) == 42

def test_put():
    t = ht.createHashTable(hash, initialCapacity=10)
    ht.put(t, "a", 1)
    ht.put(t, "b", 2)
    assert ht.size(t) == 2
    assert ht.get(t, "a") == 1
    assert ht.get(t, "b") == 2
    ht.put(t, "a", 100)
    assert ht.size(t) == 2
    assert ht.get(t, "a") == 100
    def const_hash(x):
        return 5
    t2 = ht.createHashTable(const_hash, initialCapacity=10)
    ht.put(t2, "first", 1)
    ht.put(t2, "second", 2)
    ht.put(t2, "third", 3)
    assert ht.size(t2) == 3
    bucket = t2.m[5]
    cnt = 0
    node = bucket
    values = []
    while node:
        values.append(node.data[1])
        cnt += 1
        node = node.next
    assert cnt == 3
    assert set(values) == {1, 2, 3}
    t3 = ht.createHashTable(hash, initialCapacity=5)
    t3.alpha = 0.5
    for i in range(10):
        ht.put(t3, f"k{i}", i)
    for i in range(10):
        assert ht.get(t3, f"k{i}") == i
    assert t3.capacity >= 10

def test_get():
    t = ht.createHashTable(hash)
    ht.put(t, "x", 10)
    ht.put(t, "y", 20)
    assert ht.get(t, "x") == 10
    assert ht.get(t, "y") == 20
    assert ht.get(t, "z") is None
    ht.delete(t, "x")
    assert ht.get(t, "x") is None

def test_delete():
    def my_hash(x):
        return 0
    t = ht.createHashTable(my_hash, initialCapacity=10)
    for i in range(5):
        ht.put(t, f"key{i}", i)
    assert ht.size(t) == 5
    ht.delete(t, "key2")
    assert ht.size(t) == 4
    assert ht.contains(t, "key2") is False
    assert ht.get(t, "key2") is None
    for i in range(5):
        if i != 2:
            assert ht.get(t, f"key{i}") == i
    ht.delete(t, "key0")
    assert ht.size(t) == 3
    assert ht.contains(t, "key0") is False
    ht.delete(t, "key4")
    assert ht.size(t) == 2
    assert ht.contains(t, "key4") is False
    ht.delete(t, "missing")
    assert ht.size(t) == 2
    t2 = ht.createHashTable(hash)
    ht.delete(t2, "anything")
    assert ht.size(t2) == 0

def test_contains():
    t = ht.createHashTable(hash)
    ht.put(t, "apple", 5)
    assert ht.contains(t, "apple") is True
    assert ht.contains(t, "orange") is False
    ht.delete(t, "apple")
    assert ht.contains(t, "apple") is False

def test_size():
    t = ht.createHashTable(hash)
    assert ht.size(t) == 0
    ht.put(t, "a", 1)
    assert ht.size(t) == 1
    ht.put(t, "b", 2)
    assert ht.size(t) == 2
    ht.put(t, "a", 10)
    assert ht.size(t) == 2
    ht.delete(t, "a")
    assert ht.size(t) == 1

def test_isEmpty():
    t = ht.createHashTable(hash)
    assert ht.isEmpty(t) is True
    ht.put(t, "k", "v")
    assert ht.isEmpty(t) is False
    ht.delete(t, "k")
    assert ht.isEmpty(t) is True

def test_traverse():
    t = ht.createHashTable(hash)
    collected = []
    def collect(pair):
        collected.append(pair)
        return pair
    ht.traverse(t, collect)
    assert collected == []
    data = [("one", 1), ("two", 2), ("three", 3)]
    for k, v in data:
        ht.put(t, k, v)
    collected = []
    ht.traverse(t, collect)
    assert len(collected) == 3
    assert set(collected) == set(data)
    count = 0
    def counter(pair):
        nonlocal count
        count += 1
        return pair
    ht.traverse(t, counter)
    assert count == 3

def test_mixed_key_types():
    t = ht.createHashTable(hash)
    ht.put(t, 42, "answer")
    ht.put(t, "hello", "world")
    ht.put(t, (1, 2), "tuple")
    assert ht.get(t, 42) == "answer"
    assert ht.get(t, "hello") == "world"
    assert ht.get(t, (1, 2)) == "tuple"
    assert ht.contains(t, 42) is True
    assert ht.contains(t, "42") is False
    assert ht.size(t) == 3

def test_resize_and_rehash():
    t = ht.createHashTable(lambda x: hash(x), initialCapacity=4)
    keys = [f"k{i}" for i in range(10)]
    for i, k in enumerate(keys):
        ht.put(t, k, i)
    for i, k in enumerate(keys):
        assert ht.get(t, k) == i
    assert t.capacity >= 8
    assert ht.size(t) == 10

def tests():
    test_createHashTable()
    test_put()
    test_get()
    test_delete()
    test_contains()
    test_size()
    test_isEmpty()
    test_traverse()
    test_mixed_key_types()
    test_resize_and_rehash()

if __name__ == '__main__':
    tests()