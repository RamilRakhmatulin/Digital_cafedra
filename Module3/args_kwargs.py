from translator.data import DICT
from translator.service import get_translation


def test(a, b, *args, is_test=True, **kwargs):
    print("просто a b = ", a, b)
    print("args = ", args)
    print("is_test = ", is_test)
    print("kwargs = ", kwargs)


test(1, 2, 3, 4, 5, is_test=False, message="вышел зайчик погулять ")


def get_word_translation(*args, **kwargs):
    print(args)
    print(kwargs)
    local_dict = dict(**DICT, **kwargs)
    lst = [1, 2, 3]
    test_lst = [*args, *lst]
    print(test_lst)
    results = []
    for arg in args:
        results.append(get_translation(arg, local_dict))
    return results


print(get_word_translation("son", "mother", "clock", clock="часы", key="ключ"))
