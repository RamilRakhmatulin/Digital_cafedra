import re

text = (
    "Добрый вечер! меня зовут Рамиль, моя электронная"
    "почта rrahmatulin852@gmail.com, моя рабочая почта "
    "q096-10-rakhmatulin-ramil@yandex.ru"
)

result = re.finditer(r"[\w\d_-]+@[\w\-_\d]+\.\w+", text, re.MULTILINE)
# print(result.group(0))
for item in result:
    print(item.group(0))

text2 = "03/29/2022"
print(re.sub(r"(\d{2})/([0-3]\d)/([0-9]{4})", r"\2/\1/\3", text2))
result2 = re.search(r"(\d{2})/([0-3 ]\d)/([0-9]{4})",  text2, re.MULTILINE)
print("Day: ", result2.group(2))
print("Mounth: ", result2.group(1))
print("Year: ", result2.group(3))
