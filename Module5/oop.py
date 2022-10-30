import random


class Animal():
    _count = 0
    force = 1

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color
        self.fullness = 0
        Animal._count += 1

    def eat(self, fullness=1):
        print(f"{self.__name} поел")
        self.fullness += fullness

    def __str__(self):
        return f"Животное  {self.__name}"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def say(self):
        print(f"{self.__name} говорит")

    @staticmethod
    def get_count():
        return Animal._count

    def __add__(self, other):
        if self.force > other.force:
            winner_name = self.get_name()
        elif self.force < other.force:
            winner_name = other.get_name()
        else:
            winner_name = random.choice([self.get_name(), other.get_name()])
        print("Win ", winner_name)




class Cat(Animal):
    force = 2
    def __str__(self):
        return f"Koт {self.get_name()}"

    def say(self):
        print(f"{self.get_name()} мяу")

    def mur(self):
       print(f"{self.get_name()} мур")

vasya = Cat("Вася", 5, "Черный")
barsik = Cat("Барсик", 8, "Рыжий")

# print(vasya.name, vasya.color)
# print(barsik.name, barsik.color, barsik.fullness)
barsik.eat(3)
barsik.eat()
barsik.eat()
print(barsik.fullness)
print(vasya)
vasya.set_name("Вася крутой")
print(vasya.get_name())
vasya.say()
vasya.mur()

print(Cat.get_count())
print(vasya+barsik)

parrot = Animal("Кеша", 3, "Красный")
print(parrot)
parrot.say()
parrot + vasya

class Divice():
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return self.name

class Phone(Divice):
    def make_a_call(self, phone_number):
        print(f"Звони на {phone_number}")

    def take_a_photo(self):
        print(f"{self.name}: фотография ")

class PhotoCamera(Divice):
    def take_video(self):
        print("записывает видео")
    def take_a_photo(self):
        print(f"{self.name}: фотография ")

objs = [Phone("samsung"), PhotoCamera("canon")]
for obj in objs:
    obj.take_a_photo()