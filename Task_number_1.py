# Задание №1

def Calculator(x, y, sign):
    result = x
    if sign == '+': result += y
    elif sign == '-': result -= y
    elif sign == '*': result *= y
    elif sign == '/':
        if y == 0:
            # print('Error, Деление на 0!')
            return "Error, Деление на 0!"
        else: result /= y
    elif sign == '^': result **= y
    elif sign == '%': result %= y
    elif sign == 's': result **= (1/y)
    else: print('Error')
    return result

stop = ''
res = None
while stop != '=':
    if res != None: print(f"\nПромежуточный результат = {res}")
    print('\n-----Калькулятор-----\n'
          '\'+\' - сложение\n'
          '\'-\' - вычитание\n'
          '\'*\' - умножение\n'
          '\'/\' - деление\n'
          '\'^\' - возведение в степень\n'
          '\'%\' - остаток от деления\n'
          '\'s\' - извлечение корня\n'
          'Введите действие: ', end=" ")
    if res == None:
        sign = input()
        print('Введите первое число', end=": ")
        x = int(input())
        print('Введите второе число', end=": ")
        y = int(input())
        res = Calculator(x, y, sign)
    else:
        sign = input()
        x = res
        print('Введите второе число', end=": ")
        y = int(input())
        res = Calculator(x, y, sign)

    print(f'\nРезультат = {res}'
          '\nЕсли вы завершили расчеты, введите "="\n'
          'Для продолжения подсчета нажмите Enter\n'
          'Ваше действие: ', end=" ")
    stop = input()
    print("----------------------------------")
print(f"Конечный результат: {res}")
