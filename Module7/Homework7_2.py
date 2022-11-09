import requests
import bs4
import re


def regular_today(text):
    tday= re.search(
            r"(Сегодня)([0-9]+)([А-я]+)(днём)([+-]*[0-9]+)(ночью)([+-]*[0-9]+)",text, re.MULTILINE
        )
    results=[]
    for it in range(1,8):
        results.append(tday.group(it))
    return results


def regular_day(text):
    day = re.search(
        r"([А-я]+)([0-9]+)([А-я]+)(.*.*?[0-9]+)(.*.*[0-9]+)", text, re.MULTILINE
    )
    results = []
    for it in range(1, 6):
        results.append(day.group(it))
    return results
def week_dict(w_key):
    dict={
        "Пн":"Понедельник",
        "Вт": "Вторник",
        "Ср": "Среда",
        "Чт": "Четверг",
        "Пт": "Пятница",
        "Сб": "Суббота",
        "Вс": "Воскресенье",
        "Сегодня":"Сегодня"
    }
    result = dict[w_key]
    return result


def moun_dict(m_key):
    dict = {
        "янв": "января",
        "фев": "февраля",
        "март": "марта",
        "апр": "апреля",
        "май": "мая",
        "июнь": "июня",
        "июль": "июля",
        "авг": "августа",
        "сен": "сентября",
        "окт": "октября",
        "нояб": "ноября",
        "дек": "декабря",

    }
    result = dict[m_key]
    return result

def print_weather(day):
    print(week_dict(day[0]),"  ",day[1],"  ",moun_dict(day[2]))
    print("\t","Днём",":  ",day[3])
    print("\t","Ночью",":  ",day[4])


search = input("Введите город:")
city = requests.get(f"https://alextyurin.ru/2014/04/географические-координаты-основных/")
tree = bs4.BeautifulSoup(city.text, 'html.parser')
buf = ''
for item in tree.select('#myTable'):
    buf = item.text

geograf = buf.split("\n")


city_cpl=''
shirota=''
dolgota=''
try:
    index = geograf.index(f'{search}')
    city_cpl = geograf[index]
    shirota = geograf[index + 1]
    dolgota = geograf[index + 2]
except ValueError:
    print(f"К сожалению данные о городе {search} получить невозможно")
    exit()

weather = requests.get(f"https://yandex.ru/pogoda/?lat={shirota}&lon={dolgota.strip()}&via=spr")
tree2 = bs4.BeautifulSoup(weather.text, 'html.parser')
buf_text = ''

for item2 in tree2.select('li'):
    buf_text = buf_text + item2.text.replace(" ", "") + "\n"

result = re.finditer(r"Сегодня+[\w]+[+,-,\w]+", buf_text, re.MULTILINE)
today = ''
for item in result:
    today = item.group(0)

information = buf_text.split("\n")
index_weather = information.index(today)

day1=regular_today(information[index_weather])
day2=regular_day(information[index_weather+1])
day3=regular_day(information[index_weather+2])
day4=regular_day(information[index_weather+3])
day5=regular_day(information[index_weather+4])
day6=regular_day(information[index_weather+5])
day7=regular_day(information[index_weather+6])

day1.remove('днём')
day1.remove('ночью')
print_weather(day1)
print_weather(day2)
print_weather(day3)
print_weather(day4)
print_weather(day5)
print_weather(day6)
print_weather(day7)



