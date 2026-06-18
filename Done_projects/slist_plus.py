class Slist:
    pass


def length(lst):  # Проверено
    if lst == None:
        return 0
    len_lst = 1
    while lst.next != None:
        len_lst += 1
        lst = lst.next

    return len_lst


def prepend(lst, data):  # Проверено
    new_head = Slist()
    new_head.data = data
    new_head.next = lst
    new_head.prev = None

    return new_head


def get(lst, index):  # Проверено
    if lst == None or index > length(lst):
        return None
    for i in range(index):
        lst = lst.next

    return lst.data


def remove(lst, index):  # Проверено
    ls_l = length(lst)
    if lst == None or index > ls_l:
        return None, lst
    if index == 0:
        if ls_l != 1:
            lst.next.prev = None
        return lst.data, lst.next
    else:
        head = lst
        for i in range(index - 1):
            lst = lst.next
        dat = lst.next.data
        lst.next = lst.next.next
        lst.next.prev = lst
        return dat, head


def append(lst, data):  # Проверено
    if lst == None:
        a = Slist()
        a.next = None
        a.data = data
        a.prev = None
        return a
    head = lst
    new_head = Slist()
    new_head.data = data
    new_head.next = None
    while lst.next != None:
        lst = lst.next
    lst.next = new_head
    new_head.prev = lst

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
    if lst == None:
        return None
    head = lst
    flag = 0
    while lst != None and not flag:
        if lst.prev != None:
            if lst.data == data:
                lst.prev.next = lst.next
                if lst.next != None:
                    lst.next.prev = lst.prev
                flag = 1
        else:
            if lst.data == data:
                if lst.next != None:
                    lst.next.prev = None
                head = lst.next
                flag = 1
        lst = lst.next

    return head


def remove_all(lst, data):  # NeПроверено
    if lst == None:
        return None
    head = lst
    while lst != None:
        if lst.prev != None:
            if lst.data == data:
                lst.prev.next = lst.next
                if lst.next != None:
                    lst.next.prev = lst.prev
        else:
            if lst.data == data:
                if lst.next != None:
                    lst.next.prev = None
                head = lst.next
        lst = lst.next

    return head


def copy(lst):  # Проверено
    if lst == None:
        return None
    copied = Slist()
    head = copied
    head.prev = None
    while lst.next != None:
        copied.data = lst.data
        copied_next = Slist()
        copied.next = copied_next
        copied.next.prev = copied
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
    head.prev = None
    for i in list[:-1]:
        lst.data = i
        lst.next = Slist()
        lst.next.prev = lst
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
