import random

# dct = {"a": 1}
#
# try:
#     print(dct["b"])
# except KeyError as e:
#     print("key no have", e)
#
#
# try:
#     number = int(input())
#     number2 = int(input())
#     print(number/number2)
# except (ZeroDivisionError, ValueError) as e:
#     print("введены неправельные данные ", e)
#     # print("на ноль делить нельзя")
# except BaseException as e:
#     print("произошла неизвестная ошибка ")
#     print(e)
#     print(type(e))
class AppException(Exception):
    pass

class MyException(AppException):
    def __init__(self, message ):
        self.message = message

    def __str__(self):
        return self.message


def my_func():
    if random.random() > 0.5 and random.random() < 0.7 :
        raise MyException("test")
    elif random.random() < 0.7:
        raise AppException()
    else:
        raise BaseException

for i in range(10):
    print(i)
    try:
        my_func()
    except MyException:
        print("my")
        # ... 1
    except AppException:
        print("app")
        # ...2
    except BaseException:
        print("base")
        # ..3