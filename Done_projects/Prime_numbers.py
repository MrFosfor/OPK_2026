def prime(number):
    k = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            k = False
            break
    return k

n = int(input("Введите число\n"))

if n >= 2:
    storage = [2]
    for i in range(3, n + 1, 2):
        #print("i is:", i, "sqrt for i is:", i ** 0.5, "int sqrt is:", int(i ** 0.5))
        if prime(i):
            storage.append(i)
    print(storage)