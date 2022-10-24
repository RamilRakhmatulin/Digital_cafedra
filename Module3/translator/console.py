# from .service import prepar_word
from service import prepar_word


def get_parametrs():
    word = input("Введите слово для перевода: ")
    word = prepar_word(word)
    if ord(word[0]) >= ord("a") and ord(word[0]) <= ord("z"):
        direction = 1
    elif ord(word[0]) >= ord("а") and ord(word[0]) <= ord("я"):
        direction = 2
    else:
        direction = 1
    # print("Выбирете направление перевода:")
    # print("1 с английского на русский ")
    # print("2 с русского на английский")
    # direction = input()
    #  if not direction:
    #      direction = 1
    # direction=int(direction)
    return word, direction


def print_translation(word, translation):
    if translation:
        print(f"Перевод слова {word} - {translation}")
    else:
        print(f"Нет первода для слова {word}")
