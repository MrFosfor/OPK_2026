def my_strstr(needle, haystack):
    index = -1
    len_needle = len(needle)
    if len(haystack) >= len_needle != 0:
        needle_hash = hash_func(needle)
        haystack_hash = hash_func(haystack[:len_needle])
        if haystack_hash == needle_hash:
            index += 1
        else:
            for ind in range(len(haystack) - len_needle):
                if needle_hash != haystack_hash:
                    haystack_hash -= ord(haystack[ind]) * 256 ** (len_needle - 1)
                    haystack_hash *= 256
                    haystack_hash += ord(haystack[ind + len_needle])
                else:
                    if haystack[ind:ind + len_needle] == needle:
                        index += ind + 1
                        break
    return index


def hash_func(string):
    myhash = 0
    length = len(string)
    for i in range(length):
        myhash += ord(string[i]) * 256 ** (length - i - 1)
    return myhash


def test_strstr():
    assert my_strstr("", "") == -1
    assert my_strstr("abc", "ab") == -1
    assert my_strstr("", "abc") == -1
    assert my_strstr("bvf", "abc") == -1
    assert my_strstr("abc", "abc") == 0
    assert my_strstr("gs", "fasgsjfqkc") == 3


if __name__ == '__main__':
    test_strstr()
    print(my_strstr("cxc", "tuyufsvhfuasdgyinthbwenczcxcyu"))  # == 25
    print(my_strstr("68", "527168746"))  # == 4
