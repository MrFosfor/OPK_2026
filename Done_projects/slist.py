class Slist:
    pass


def length(lst):  # Проверено
    len_lst = 0
    flag = 0
    if lst != None:
        flag = 1
        len_lst += 1
    while flag and lst.next != None:
        len_lst += 1
        lst = lst.next

    return len_lst


def prepend(lst, data):  # Проверено
    new_head = Slist()
    new_head.data = data
    new_head.next = lst

    return new_head


def get(lst, index):  # Проверено
    if lst == None or index > length(lst):
        return None
    for i in range(index):
        lst = lst.next

    return lst.data


def remove(lst, index):  # Проверено
    if lst == None or index > length(lst) - 1:
        return None, lst
    if index == 0:
        return lst.data, lst.next
    else:
        head = lst
        for i in range(index - 1):
            lst = lst.next
        dat = lst.next.data
        lst.next = lst.next.next
        return dat, head


def append(lst, data):  # Проверено
    if lst == None:
        a = Slist()
        a.next = None
        a.data = data
        return a
    head = lst
    new_head = Slist()
    new_head.data = data
    new_head.next = None
    while lst.next != None:
        lst = lst.next
    lst.next = new_head

    return head


def get_last(lst):  # Проверено
    if lst == None:
        return None
    while lst.next != None:
        lst = lst.next

    return lst.data


def find(lst, data):  # Проверено
    flag = -1
    counter = 0;
    while lst != None:
        if lst.data == data:
            flag = counter
            break
        counter += 1
        lst = lst.next

    return flag


def remove_first(lst, data):  # проверено
    flag = 1
    head = lst
    if lst == None:
        return None
    if head.data == data:
        head = lst.next
        flag = 0
    while lst.next != None and flag:
        if lst.next.data == data:
            lst.next = lst.next.next
            break
        else:
            lst = lst.next

    return head


def remove_all(lst, data):  # Проверено
    head = lst
    flag = 0
    prev = Slist()
    while lst != None:
        if lst.data == data:
            if not flag:
                head = lst.next
                lst = lst.next
            else:
                prev.next = lst.next
                lst = lst.next
        else:
            prev = lst
            lst = lst.next
        if lst != None and lst.data != data:
            flag = 1

    return head


def copy(lst):  # Проверено
    if lst == None:
        return None
    copied = Slist()
    head = copied
    while lst.next != None:
        copied.data = lst.data
        copied_next = Slist()
        copied.next = copied_next
        lst = lst.next
        copied = copied.next
    copied.data = lst.data
    copied.next = None

    return head


def concat(lst1, lst2):  # Проверено
    if lst1 == None:
        return lst2
    if lst2 == None:
        return lst1
    head = copy(lst1)
    copy_f = head
    while copy_f.next != None:
        copy_f = copy_f.next
    copy_f.next = copy(lst2)

    return head


def foreach(lst, func):  # Проверено
    while lst != None:
        lst.data = func(lst.data)
        lst = lst.next


def find_custom(lst, predicate):  # Проверено
    flag = 0
    counter = 0
    while lst != None:
        if predicate(lst.data):
            return lst.data, counter
        counter += 1
        lst = lst.next

    return None, -1


def from_list(list):  # Проверено
    if len(list) == 0:
        return None
    lst = Slist()
    head = lst
    for i in list[:-1]:
        lst.data = i
        lst.next = Slist()
        lst = lst.next
    lst.next = None
    lst.data = list[-1]
    return head


def to_list(lst):  # Проверено
    list = []
    while lst != None:
        list.append(lst.data)
        lst = lst.next
    return list
