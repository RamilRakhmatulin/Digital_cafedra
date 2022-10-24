from data import DICT, REVERSED_DICT
from console import get_parametrs, print_translation
from service import get_translation

while True:
    word, direction = get_parametrs()
    if direction == 1:
        translation = get_translation(word, DICT)
        print_translation(word, translation)
    else:
        translation = get_translation(word, REVERSED_DICT)
        print_translation(word, translation)
