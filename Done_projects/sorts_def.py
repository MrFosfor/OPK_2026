from random import randint


class Students:
    def __init__(self, name, age, group, score):
        self.name = name
        self.age = age
        self.group = group
        self.score = score

    def describe(self):
        print(f'Имя: {self.name}, Возраст: {self.age}, Группа: {self.group}, Балл: {self.score}')


def key_func(value):
    return value


def bubble_sort(arr, key=key_func):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def heap_sort(arr, key=key_func):
    length = len(arr)
    for i in range(length, -1, -1):
        heapify(arr, key, length, i)
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, key, i, 0)


def heapify(arr, key, length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < length and key(arr[largest]) < key(arr[left]):
        largest = left
    if right < length and key(arr[largest]) < key(arr[right]):
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, key, length, largest)


def selection_sort(arr, key=key_func):
    size = len(arr)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if key(arr[j]) < key(arr[min_index]):
                min_index = j
        arr[ind], arr[min_index] = arr[min_index], arr[ind]


def insertion_sort(arr, keyf=key_func):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and keyf(key) < keyf(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def sort_test():
    check_array(randomized_array(2))
    check_array(randomized_array(5))
    check_array(randomized_array(10))
    check_array(randomized_array(50, -100, 100))
    check_array(randomized_array(1000, -1000, 1000))

    # data = {"Sorted data": [0, 1, 2, 2, 4, 5, 7, 8, 12, 19],
    #         "Non sorted data": [2, 5, 2, 8, 19, 12, 4, 7, 1, 0],
    #         "Reversed data": [19, 12, 8, 7, 5, 4, 2, 2, 1, 0],
    #         "Empty data": [],
    #         "One elem": [1],
    #         "Two elems": [2, 1]}
    # for name, arr in data.items():
    #     separator(37)
    #     print(name)
    #     print("Origin:", arr)
    #     sort_func(arr, key_func)
    #     print("Sorted:", arr)
    #
    # print('-' * 12, "Random data", "-" * 12, )
    # number, start, end = input("Enter Length of array, Start and End of rand range (format - N N N): ").split()
    # number, start, end = int(number), int(start), int(end)
    # arr = randomized_array(number, start, end)
    # print("Randomized origin:", arr)
    # sort_func(arr, key_func)
    # print("Randomized sorted:", arr)
    # print('-' * 15, "Done!", "-" * 15, "\n")


def check_array(arr, key=key_func):
    sorts = [bubble_sort, selection_sort, insertion_sort, heap_sort]
    for sr in sorts:
        base = arr
        sr(base)
        for i in range(1, len(base)):
            assert (key(base[i]) >= key(base[i - 1]))


def randomized_array(number=10, start=-50, end=50):
    arr = []
    for _ in range(number):
        arr.append(randint(start, end))
    return arr


def separator(num):
    print("-" * num)


def class_print(stud_data):
    separator(37)
    for i in range(len(stud_data)):
        stud_data[i].describe()

if __name__ == '__main__':
    sort_test()

# if int(input("Choose function for check: Bubble - 1, Heap - 0: ")):
#     sort_test(bubble_sort)
# else:
#     sort_test(heap_sort)
#
# names, ages, groups, scores = (["Полина", "Анна", "Николай", "Тимофей", "Александр"],
#                             [21, 17, 18, 18, 19], [23315, 25316, 25313, 25315, 25315],
#                             [105, 78, 67, 67, 32])
# stud_data = []
# for i in range(len(names)):
#     stud_data.append(Students(names[i], ages[i], groups[i], scores[i]))
# class_print(stud_data)
# heap_sort(stud_data, key_func)
# class_print(stud_data)
