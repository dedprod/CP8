def convert(chis):
            b=''
            while chis>0:
                    b=str(chis % x) + b
                    chis=chis//x
            print(b)
try:
    print("Введите желаемую систему счисления до 9")
    x=int(input())
    print("Введите число для перевода")
    chis=int(input())
except ValueError:
    print("Incorrect value")
    exit()
if (x<10) & (chis> -1):
    convert(chis)
else:
    print("Данная система счисления или число пока что не поддерживается, пожалуйста введите другое значение")
