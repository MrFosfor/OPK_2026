import sorts_def as fs
from random import randint
from time import perf_counter_ns


def key(value):
    return value


def key_1(value):
    return value


def key_2(value):
    return -value


def data(matrix):
    for _ in range(3):
        temp = []
        for i in range(1, 5):
            temp.append(fs.randomized_array(10 ** i, -10000, 10000))
        matrix.append(temp)

    for mass in matrix[1]:
        fs.heap_sort(mass, key_1)
        l = len(mass)
        for i in range(l // 5):
            x, y = randint(0, l - 1), randint(0, l - 1)
            mass[x], mass[y] = mass[y], mass[x]

    for mass in matrix[2]:
        fs.heap_sort(mass, key_2)


def measure():
    matrix = []
    results = []
    data(matrix)
    for i in range(len(matrix)):
        temp = []
        for j in range(4):
            temp.append(time_mess(matrix[i][j]))
        results.append(temp)
    print_result(results)


def time_mess(array):
    answer = [0] * 4
    sorts = [fs.bubble_sort, fs.selection_sort, fs.insertion_sort, fs.heap_sort]
    for i in range(4):
        start = perf_counter_ns()
        sorts[i](array, key)
        finish = perf_counter_ns()
        answer[i] += (finish - start) / 10 ** 6
    return answer


def print_result(results):
    print("-------- Результаты измерения --------")
    # sort_mass = ["Пузырек", "Выбором", "Вставками", "Пирамидальная"]
    mass_type = ["Рандомный массив", "Случайная замена", "Обратный массив"]
    print("Сортировки:\n[Пузырьком, Выбором, Вставками, Пирамидальная]")
    # fs.separator(38)

    for i in range(len(results)):
        print(f'\t\t----- {mass_type[i]} -----')
        for j in range(len(results[i])):
            print(f'Массив длины {10 ** (j + 1)}:')
            print(results[i][j])
            fs.separator(38)
        print()

if __name__ == '__main__':
    measure()

