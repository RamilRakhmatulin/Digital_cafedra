def input_output(func):
    def wrapper(*args, **kwargs):
        if len(args) == 0 and len(kwargs) == 0:
            print("На вход ничего не вводится ")
        elif len(args) == 0:
            print("Функция принимает на ввод :  ", kwargs)
        elif len(kwargs) == 0:
            print("Функция принимает на ввод :  ", args)
        else:
            print("Функция принимает на ввод :  ", args, kwargs)

        print("Функция выводит : ", func(*args, **kwargs))

    return wrapper


@input_output
def example(*args, **kwargs):
    a = args
    return (a)


# decorated_div = zero_div_handler_decorator(div)
example(4, 2, rabbit="кролик")
example(2, 1)
example(twenty_one="42/2")
example()
