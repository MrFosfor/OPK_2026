def is_balanced(string):
    flag = True
    array = []
    for i in string:
        if i == "(" or i == "[" or i == "{" or i == "<":
            array.append(i)
        elif i == ")" or i == "]" or i == "}" or i == ">":
            if len(array) > 0:
                simbol = array.pop()
                match simbol:
                    case "(":
                        if i != ")":
                            flag = False
                            break
                    case "[":
                        if i != "]":
                            flag = False
                            break
                    case "{":
                        if i != "}":
                            flag = False
                            break
                    case "<":
                        if i != ">":
                            flag = False
                            break
            else:
                flag = False
    if len(array) != 0:
        flag = False

    return flag


print("\n", is_balanced(input("Введите строку для проверки:\n")), sep="")