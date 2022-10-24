# from translator.console import get_parametrs, print_translation
# from translator.data import DICT, REVERSED_DICT
# from translator.service import get_translation
from translator import (
    get_parametrs,
    print_translation,
    DICT,
    REVERSED_DICT,
    get_translation
)

while True:
    word, direction = get_parametrs()
    if direction == 1:
        translation = get_translation(word, DICT)
        print_translation(word, translation)
    else:
        translation = get_translation(word, REVERSED_DICT)
        print_translation(word, translation)
