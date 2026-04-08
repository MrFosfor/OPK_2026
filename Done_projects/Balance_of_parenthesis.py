def is_balanced(string):
    flag = True
    array = []
    for i in string:
        if i == "(":
            array.append(i)
        elif i == ")":
            if len(array) > 0:
                array.pop()
            else:
                flag = False
                break
    if len(array) != 0:
        flag = False

    return flag


print("\n", is_balanced(input("Введите строку для проверки:\n")), sep="")