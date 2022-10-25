def my_genetor():
    print("Старт генератора")
    i = 1
    while True:
        print("Итерация генератора", i)
        i += 1
        yield i ** 2

my_genetor2=(i**2 for i in range(100))
print(list(my_genetor2))

for i in my_genetor():
    print("в цикле", i)
    if i > 100:
        break
