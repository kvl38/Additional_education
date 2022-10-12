# Задание №1

def Calculator(x, y, sign):
    result = x
    if sign == '+': result += y
    elif sign == '-': result -= y
    elif sign == '*': result *= y
    elif sign == '/':
        if y == 0:
            return "Error, Деление на 0!"
        else: result /= y
    elif sign == '^': result **= y
    elif sign == '%':
        if y == 0:
            return "Error, Деление на 0!"
        else: result %= y
    elif sign == 's': result **= (1/y)
    else: print('Error')
    return result

def Ent_values(result):
    if result == None:
        sign = input()
        print('Введите первое число', end=": ")
        x = int(input())
        if sign == '^':
            print('Введите степень числа', end=": ")
        elif sign == 's':
            print('Введите степень корня числа', end=": ")
        else:
            print('Введите второе число', end=": ")
        y = int(input())
        result = Calculator(x, y, sign)
    else:
        sign = input()
        x = result
        if sign == '^':
            print('Введите степень числа', end=": ")
        elif sign == 's':
            print('Введите степень корня числа', end=": ")
        else:
            print('Введите второе число', end=": ")
        y = int(input())
        result = Calculator(x, y, sign)
    return result


if __name__ == '__main__':
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

        res = Ent_values(res)

        print(f'\nРезультат = {res}'
              '\nЕсли вы завершили расчеты, введите "="\n'
              'Для продолжения подсчета нажмите Enter\n'
              'Ваше действие: ', end=" ")
        stop = input()
        print("----------------------------------")
    print(f"Конечный результат: {res}")
