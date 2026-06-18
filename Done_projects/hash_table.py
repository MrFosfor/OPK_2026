import slist_plus as slist


class HashTable:
    pass


def createHashTable(hashFunction, initialCapacity=100):
    table = HashTable()
    table.hash = hashFunction
    table.capacity = initialCapacity
    table.size = 0
    table.m = [None for _ in range(initialCapacity)]
    table.alpha = 0.75
    return table


def _hash(hashTable, key):
    return abs(hashTable.hash(key)) % hashTable.capacity


def _resize(hashTable):
    old_buckets = hashTable.m
    hashTable.capacity *= 2
    hashTable.m = [None for _ in range(hashTable.capacity)]
    for bucket in old_buckets:
        if bucket is not None:
            items = slist.to_list(bucket)
            for key, value in items:
                keyHash = _hash(hashTable, key)
                if hashTable.m[keyHash] is None:
                    hashTable.m[keyHash] = slist.from_list([(key, value)])
                else:
                    slist.append(hashTable.m[keyHash], (key, value))


def put(hashTable, key, value):
    keyHash = _hash(hashTable, key)
    data = hashTable.m[keyHash]
    if data is None:
        hashTable.m[keyHash] = slist.from_list([(key, value)])
        hashTable.size += 1
    else:
        lst = data
        flag = 1
        while flag and lst is not None:
            if lst.data[0] == key:
                lst.data = (key, value)
                flag = 0
            else:
                lst = lst.next
        if flag:
            slist.append(data, (key, value))
            hashTable.size += 1
    if hashTable.size / hashTable.capacity > hashTable.alpha:
        _resize(hashTable)


def get(hashTable, key):
    keyHash = _hash(hashTable, key)
    node = hashTable.m[keyHash]
    while node is not None:
        if node.data[0] == key:
            return node.data[1]
        else:
            node = node.next
    return None


def delete(hashTable, key):
    keyHash = _hash(hashTable, key)
    node = hashTable.m[keyHash]
    prev = None
    while node:
        if node.data[0] == key:
            if prev is None:
                hashTable.m[keyHash] = node.next
            else:
                prev.next = node.next
            hashTable.size -= 1
            return
        prev = node
        node = node.next


def contains(hashTable, key):
    keyHash = _hash(hashTable, key)
    node = hashTable.m[keyHash]
    while node is not None:
        if node.data[0] == key:
            return True
        else:
            node = node.next
    return False


def size(hashTable):
    return hashTable.size


def isEmpty(hashTable):
    return hashTable.size == 0


def traverse(hashTable, func):
    for i in range(hashTable.capacity):
        if hashTable.m[i] is not None:
            slist.foreach(hashTable.m[i], func)
