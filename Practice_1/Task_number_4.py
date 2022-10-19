# Задание №4

import time

def Timer():
    hours = int(input("Введите количество часов: "))
    minutes = int(input("Введите количество минут: "))
    seconds = int(input("Введите количество секунд: "))
    input("Нажмите Enter для запуска таймера")
    line = "-" * 37
    print("\n"+line)
    while not (hours == minutes == seconds == 0):
        if seconds == 0:
            seconds = 60
            if minutes == 0:
                minutes = 60
                hours -= 1
            minutes -= 1

        print("Осталось: ", hours, " часов, ", minutes, " минут, ", seconds, " секунд", sep="")
        seconds -= 1
        time.sleep(1)
    print(line)

if __name__ == '__main__':
    Timer()

    input()
