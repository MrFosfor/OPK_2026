day, month, year = input("Введите дату в формате: DD MM YYYY\n").split(" ")
day, month, year = int(day), int(month), int(year)

is_data_true = False
is_leap = False

# print(year % 4 == 0, year % 100 != 0, year % 400 == 0)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    is_leap = True

if month <= 12 and day <= 31:
    is_data_true = True

if month % 2 == 1 and day > 30 and is_data_true:
    is_data_true = False
elif month % 2 == 0 and day > 31 and is_data_true:
    is_data_true = False

if month == 2 and is_data_true:
    if is_leap:
        if day > 29:
            is_data_true = False
    else:
        if day > 28:
            is_data_true = False

if is_data_true:
    number_of_day = 0
    for i in range(1, month):
        # print("test num1:", number_of_day)
        if i == 2:
            if is_leap:
                number_of_day += 29
            else:
                number_of_day += 28
        elif i % 2 == 1:
            number_of_day += 31
        else:
            number_of_day += 30
    print(number_of_day + day)
else:
    print("Неверная дата.")