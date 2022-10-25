lst_console = (input("Введите числа через пробел: "))
bufer = [i for i in lst_console.split(" ") if i != ""]
numbers = []
try:
    numbers = [int(i) for i in bufer]
except ValueError:
    print(-1)
    exit()

even_numbers_lst_comp = [i for i in numbers if i % 2 == 0]
not_even_numbers_lst_comp = [i for i in numbers if i % 2 != 0]
negative_numbers_lst_comp = [i for i in numbers if i < 0]

if len(even_numbers_lst_comp) == 0:
    print("Четных чисел нет ")
else:
    print("Четные числа с помощью list comprehensions: ", even_numbers_lst_comp)

if len(not_even_numbers_lst_comp) == 0:
    print("Нечетных чисел нет ")
else:
    print("Нечетные числа с помощью list comprehensions: ", not_even_numbers_lst_comp)

if len(negative_numbers_lst_comp) == 0:
    print("Отрицательных чисел нет ")
else:
    print("Отрицательные числа с помощью list comprehensions: ", negative_numbers_lst_comp)

print()

even_numbers_filter = list(filter(lambda x: x % 2 == 0, numbers))
not_even_numbers_filter = list(filter(lambda x: x % 2 != 0, numbers))
negative_numbers_filter = list(filter(lambda x: x < 0, numbers))

if len(even_numbers_filter) != 0:
    print("Четные числа с помощью filter: ", even_numbers_filter)

if len(not_even_numbers_filter) != 0:
    print("Нечетные числа с помощью filter: ", not_even_numbers_filter)

    if len(list(negative_numbers_filter)) != 0:
        print("Отрицательные числа с помощью filter: ", negative_numbers_filter)
