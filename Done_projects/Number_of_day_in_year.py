day, month, year = input("Введите дату в формате: DD MM YYYY\n").split(" ")
day, month, year = int(day), int(month), int(year)

is_data_true = False
is_leap = False

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    is_leap = True

if is_leap:
    months[1] = 29

if month <= 12 and day <= 31:
    is_data_true = True

if is_data_true and months[month - 1] < day:
    is_data_true = False

if is_data_true:
    number_of_day = 0
    for i in months[:month - 1]:
        number_of_day += i
    print(number_of_day + day)

else:
    print("Неверная дата.")