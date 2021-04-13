num1 = int(input('1 число'))
num2 = int(input('2 число'))
action = input('знак')
def do(num1,num2,action):
    if action == "+":
        print(num1 + num2)
    if action == '-':
        print(num1 - num2)
    if action == '*':
        print(num1 * num2)
    if action == '/':
            print(num1 / num2)
print(do(num1,num2,action))

try:
    do(num1,num2,action)
except ValueError:
    print('некорректное значение')
except ZeroDivisionError:
    print('Нельзя делить на ноль')
except SyntaxError:
    print('синтаксическая ошибка')




