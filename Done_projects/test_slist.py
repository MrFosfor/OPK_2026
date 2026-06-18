import slist as sl
import slist_plus as sp


def predicat64(num):
    flag = False
    if num == 64:
        flag = True
    return flag


def predicat100(num):
    flag = False
    if num == 100:
        flag = True
    return flag


def foreachPowerTwo(num):
    return num ** 2


def length(s):
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    assert s.length(lst) == len(list)
    list = []
    lst = s.from_list(list)
    assert s.length(lst) == len(list)


def prepend(s):
    lst = None
    lst = s.prepend(lst, "start")
    assert s.length(lst) == 1
    assert lst.data == "start"
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    lst = s.prepend(lst, "start")
    assert s.length(lst) == len(list) + 1
    assert lst.data == "start"


def get(s):
    lst = None
    assert s.get(lst, 0) == None
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    assert s.get(lst, 0) == 0
    assert s.get(lst, 5) == 25
    assert s.get(lst, 11) == None
    assert s.to_list(lst) == list


def remove(s):
    lst = None
    assert s.remove(lst, 0) == (None, lst)
    lst = s.Slist()
    lst.next = None
    lst.data = 11
    if s == sp:
        lst.prev = None
    data, lst = s.remove(lst, 0)
    assert (data, lst) == (11, None)
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    data, lst = s.remove(lst, 11)
    assert (data, lst) == (None, lst)
    assert s.to_list(lst) == list
    data, lst = s.remove(lst, 3)
    assert (data, lst) == (9, lst)
    data, lst = s.remove(lst, 3)
    assert (data, lst) == (16, lst)
    data, lst = s.remove(lst, 0)
    assert (data, lst) == (0, lst)
    assert s.to_list(lst) == [1, 4, 25, 36, 49, 64, 81]


def append(s):
    lst = None
    lst = s.append(lst, 100)
    assert s.length(lst) == 1
    assert s.get(lst, 0) == 100
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    lst = s.append(lst, 100)
    list.append(100)
    assert s.to_list(lst) == list


def get_last(s):
    lst = None
    assert s.get_last(lst) == None
    lst = s.Slist()
    lst.data = 11
    lst.next = None
    assert s.get_last(lst) == 11
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    assert s.get_last(lst) == 81


def find(s):
    lst = None
    assert s.find(lst, 100) == -1
    list = [0, 1, 2, 3, 4, 10, 10, 10, 8, 9]
    lst = s.from_list(list)
    assert s.find(lst, 100) == -1
    assert s.find(lst, 0) == 0
    assert s.find(lst, 10) == 5


def remove_first(s):
    lst = None
    assert s.remove_first(lst, 100) == None
    list = [0, 1, 2, 3, 4, 10, 10, 10, 8, 9]
    lst = s.from_list(list)
    lst = s.remove_first(lst, 10)
    assert s.to_list(lst) == [0, 1, 2, 3, 4, 10, 10, 8, 9]
    lst = s.remove_first(lst, 1)
    assert s.to_list(lst) == [0, 2, 3, 4, 10, 10, 8, 9]
    lst = s.remove_first(lst, 100)
    assert s.to_list(lst) == [0, 2, 3, 4, 10, 10, 8, 9]
    lst = s.remove_first(lst, 10)
    assert s.to_list(lst) == [0, 2, 3, 4, 10, 8, 9]
    lst = s.Slist()
    lst.next = None
    lst.prev = None
    lst.data = 10
    lst = s.remove_first(lst, 10)
    assert lst == None
    list = [1, 2, 10]
    lst = s.from_list(list)
    lst = s.remove_first(lst, 10)
    assert s.to_list(lst) == [1, 2]


def remove_all(s):
    lst = None
    assert s.remove_first(lst, 100) == None
    lst = s.Slist()
    lst.next = None
    lst.prev = None
    lst.data = 10
    lst = s.remove_first(lst, 10)
    assert lst == None
    list = [10 for i in range(5)]
    lst = s.from_list(list)
    lst = s.remove_all(lst, 10)
    assert lst == None
    list = [0, 1, 2, 3, 4, 10, 10, 10, 8, 9]
    lst = s.from_list(list)
    lst = s.remove_all(lst, 10)
    assert s.to_list(lst) == [0, 1, 2, 3, 4, 8, 9]
    list = [10, 1, 2, 3, 4, 10, 10, 10, 8, 9]
    lst = s.from_list(list)
    lst = s.remove_all(lst, 10)
    assert s.to_list(lst) == [1, 2, 3, 4, 8, 9]
    list = [1, 2, 10, 10]
    lst = s.from_list(list)
    lst = s.remove_all(lst, 10)
    assert s.to_list(lst) == [1, 2]


def copy(s):
    lst1 = None
    lst2 = s.copy(lst1)
    lst1 = s.from_list([i ** 2 for i in range(5)])
    lst2 = s.copy(lst1)
    assert s.to_list(lst1) == s.to_list(lst2)
    lst1 = s.prepend(lst1, 15)
    assert s.to_list(lst1) != s.to_list(lst2)


def concat(s):
    lst1 = s.from_list([i ** 2 for i in range(5)])
    lst2 = s.from_list([(i + 5) ** 2 for i in range(5)])
    lst_cc = s.concat(lst1, lst2)
    assert s.to_list(lst_cc) == s.to_list(lst1) + s.to_list(lst2)


def foreach(s):
    lst = s.from_list([i for i in range(5)])
    s.foreach(lst, foreachPowerTwo)
    assert s.to_list(lst) == [i**2 for i in range(5)]

def find_custom(s):
    lst = s.from_list([i**2 for i in range(10)])
    assert s.find_custom(lst, predicat64) == (64, 8)
    assert s.find_custom(lst, predicat100) == (None, -1)
    lst = s.concat(lst, s.from_list([100 for i in range(3)]))
    assert s.find_custom(lst, predicat100) == (100, 10)

def from_list(s):
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    count = 0
    while lst != None:
        assert lst.data == list[count]
        lst = lst.next
        count += 1
    list = []
    lst = s.from_list(list)
    assert lst == None


def to_list(s):
    list = [i ** 2 for i in range(10)]
    lst = s.from_list(list)
    ls = s.to_list(lst)
    assert list == ls
    lst = None
    assert s.to_list(lst) == []


def tests(s):
    from_list(s)
    to_list(s)
    length(s)
    prepend(s)
    get(s)
    remove(s)
    append(s)
    get_last(s)
    find(s)
    remove_first(s)
    remove_all(s)
    copy(s)
    concat(s)
    foreach(s)
    find_custom(s)


if __name__ == '__main__':
    tests(sl)
    tests(sp)
