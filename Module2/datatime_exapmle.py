# import datetime
from datetime import datetime, date, timedelta
# print(datetime.date.today())
# print(datetime.date.today().strftime(
print(date.today())
print(date.today().strftime(
    "today - %d.%m.%Y"
))

print(datetime.today())
print(datetime.today().strftime(
    " %d.%m.%Y %H:%M:%S"
))

a =datetime(2001, 8, 24, 5, 34)
print(a.time())
print(a.strftime(" %d.%m.%Y %H:%M:%S"))

b= datetime.strptime(
    "08.02.2007 07:54:12",
    "%d.%m.%Y %H:%M:%S"
)

print(b)

c=a+timedelta(hours=1, minutes=30)

print(c)