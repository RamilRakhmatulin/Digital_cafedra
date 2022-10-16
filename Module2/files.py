print("Fail Main.py")
file=open("../Module1/main.py", "r")
print(file.read())
file.close()

print("Fail Variables.py")
# file=open("../Module1/variables.py", "r")
# for line in file:
#     print(line.strip())
#
# file.close()

# with open("../Module1/variables.py", "r") as file:
#     # открытие файла
#     for line in file:
#         print(line.strip())
# # закрытие файла


with open("file.txt", "w+") as file:
    file.write(str(123))
    file.seek(0)
    print(file.read())

