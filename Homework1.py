first_number=float(input("Введите первое число: "))
second_number=float(input("Введите второе число: "))
sign_calcul=input("Введите алгебраическое действие + \ - \ / \ * \ :")
plus=[]
minus=[]
division=[]
mulitiplic=[]
stop_command= " "
flag_sign= bool(1)
while stop_command!="end":
    if(first_number>=0 and second_number<0):
        str_teamplate = "{0}{2}({1}) = {3}"
    elif(first_number<0 and second_number>=0):
        str_teamplate = "({0}){2}{1} = {3}"
    elif(first_number<0 and second_number<0):
        str_teamplate = "({0}){2}({1}) = {3}"
    else:
        str_teamplate = "{0}{2}{1} = {3}"
    if(sign_calcul=="+"):
        print(str_teamplate.format(first_number, second_number, sign_calcul, first_number+second_number))
        plus.append(str_teamplate.format(first_number, second_number, sign_calcul, first_number+second_number))
    elif (sign_calcul=="-"):
        print(str_teamplate.format(first_number, second_number, sign_calcul, first_number - second_number))
        minus.append(str_teamplate.format(first_number, second_number, sign_calcul, first_number - second_number))
    elif (sign_calcul=="/"):
        if(second_number==0):
            print("происходит деление на 0, так нельзя, пожалуйста задайте новый делитель или введите end , чтобы завершить работу:  ")
            bufer=input()
            if(bufer=="end"):
                break
            else:
                second_number=float(bufer)
                print(str_teamplate.format(first_number, second_number, sign_calcul, first_number/second_number))
                division.append(str_teamplate.format(first_number, second_number, sign_calcul, first_number/second_number))
        else:
            print(str_teamplate.format(first_number, second_number, sign_calcul, first_number/second_number))
            division.append(str_teamplate.format(first_number, second_number, sign_calcul, first_number / second_number))
    elif (sign_calcul=="*"):
        print(str_teamplate.format(first_number, second_number, sign_calcul, first_number * second_number))
        mulitiplic.append(str_teamplate.format(first_number, second_number, sign_calcul, first_number * second_number))
    else:
        print("введен не коректный алгебраический знак")
        sign_calcul=input("Введите  алгебраический знак заново ")
        flag_sign=bool(0)
    if(flag_sign):
        print("+", list(reversed(plus)))
        print("-", list(reversed(minus)))
        print("/", list(reversed(division)))
        print("*", list(reversed(mulitiplic)))
        stop_command = input("для завершения введите  end иначе введите новое  первое число ")
        if (stop_command != "end"):
            first_number=float(stop_command)
            second_number = float(input("Введите второе число: "))
            sign_calcul = input("Введите алгебраическое действие + \ - \ / \ * \ : ")
    flag_sign = bool(1)