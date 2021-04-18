stroka = int(input('stroka'))
suma = 0
if isinstance(stroka,int):
    while stroka > 0:
        digit = stroka % 10
        suma = suma + digit
        stroka = stroka // 10

print("Сумма:", suma)
