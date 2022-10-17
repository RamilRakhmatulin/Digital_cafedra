import os
import shutil
from os import path
import tempfile
from pathlib import Path
comand=input("Введите команду: ")
comand_lst=comand.split(" ")
cur_path=os.getcwd()
cdcur_path=cur_path
copy=cdcur_path
buf="no"
# cd_dirs=comand_lst[1].split("/")
# print(cd_dirs)
while comand_lst[0]!="exit":
    if(comand_lst[0]=="pwd"):
        print(os.getcwd())
    elif(comand_lst[0]=="cd"):
        cd_dirs = comand_lst[1].split("/" or "\ ")
        if (cd_dirs[-1].find(".") >= 0 and cd_dirs[-1].find("..")<0):
            print("вы ввели некоректную директорию")
        else:
            copy=os.getcwd()
            cd_path = Path(os.getcwd()) / comand_lst[1]
            # try:
            #     os.chdir(Path(cdcur_path))
            # except FileNotFoundError:
            #     print("директории  ", comand_lst[1], "не существует")
            #     buf = input("хотите создать директорию ? (y/n)")
            #     if buf == "y":
            #         os.makedirs((comand_lst[1]))
            #
            # #             break
            for item in cd_dirs:
                if Path(item).exists():
                    cdcur_path=Path(cdcur_path)/item
                    os.chdir(cdcur_path)
                else:
                    if buf=="no":
                        print("директории  ", comand_lst[1], "не существует")
                        buf = input("хотите создать директорию ? (y/n)")
                    if buf=="y":
                        os.makedirs((comand_lst[1]))
                        buf="no"
                        break
                    elif buf=="n":
                        os.chdir(copy)
                        buf = "no"
                        break
    elif(comand_lst[0]=="touch"):
        path_nullfile = Path(os.getcwd()) / comand_lst[1]
        if Path(path_nullfile).exists():
            print("Такой файл уже существует")
        else:
            with path_nullfile.open("w") as file:
                print("файл создан")
    elif(comand_lst[0]=="cat"):
        path_file = Path(os.getcwd()) / comand_lst[1]
        try:
            with path_file.open("r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("Файла не существует ")

    elif (comand_lst[0] == "ls"):
        directory=os.getcwd()
        filetype = os.listdir(directory)
        filetype_copy=[]
        if (len(comand_lst) > 1):
            type =comand_lst[1] .replace('*', '')
            for f in filetype:
                if path.splitext(f)[1]==type:
                    filetype_copy.append(f)
            print(filetype_copy)
        else:
            print(filetype)
    elif (comand_lst[0] == "rm"):
        file_del = Path(os.getcwd())/ comand_lst[1]
        try:
            os.remove(file_del)
        except FileNotFoundError:
            print("Файла не существует ")

    else:
        print("Данной команды не существует ")
    comand = input("Введите команду: ")
    comand_lst = comand.split(" ")