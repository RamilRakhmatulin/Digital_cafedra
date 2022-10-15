name=input("Введите имя: ")
age=float(input("Введите возраст : "))
is_working_now =bool(int(input("Работает сейчас? (1-да 0-нет)")))

workplace = None
if is_working_now:
    workplace= input("Место работы: ")

if is_working_now and not workplace:
    print("The place of work is not filled")

print(f"Name: {name}")
print(f"Age: {age}")
print("Working now: "+str(is_working_now))
if is_working_now:
    print("Workplace: " + workplace)
if age >= 20:
    print ("The user is over 20 years old")
elif age>= 18:
    print("adult")
else:
    print("not an adult")
str_teamplate = "Information on users: {} - {}"
print(str_teamplate.format(name, age))

# print(name.upper())
# print(name.lower())
# print(name.find("m"))
# print(name.replace("l", "lka"))
# print(name)
#
# a=2
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(5//a)
#
# number=input("Введите число:")
# number= int(number)
# print(2*number)
#
# c=4
# c+=1
#
# print(c)