# Задание №5

import random

class Character:

    def get_random_name():
        bank = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890"
        name = ""
        for i in range(random.randint(1, 10)):
            name += random.choice(bank)
        return name

    def get_random_age():
        age = random.randint(1, 100)
        return age

    def get_random_class():
        list_of_classes = ['Воин', 'Маг', 'Ремесленник', 'Дварф', 'Гном', 'Оборотень']
        character_class = random.choice(list_of_classes)
        return character_class

    def get_random_parameters():
        parameters = {'Здоровье (hp)' : random.randint(0,999),
                      'Рост (см)' : random.randint(100,220),
                      'Вес (кг)' : random.randint(40,200),
                      'Обмундирование' : random.choice(['нож', 'пистолет', 'арбалет', 'меч', 'топор', 'магическая палка'])
                     }
        return parameters

    def get_random_characteristics():
        characteristics = {'сила' : random.randint(0,10),
                              'Восприятие' : random.randint(0,10),
                              'Выносливость' : random.randint(0,10),
                              'Харизма' : random.randint(0,10),
                              'Интеллект' : random.randint(0,10),
                              'Ловкость' : random.randint(0,10),
                              'Удача' : random.randint(0,10)
                          }
        return characteristics

    def get_random_skill():
        list_of_skills = ['Иммунитет к атакам', 'Истощение', 'Ураган', 'Обезвреживание', 'Бессилие', 'Бесплотность', 'Страх',
                          'Принудительное движение', 'Проклятие', 'Исчезновение', 'Гипноз', 'Невидимость', 'Неуязвимость',
                          'Оцепенение Безмолвие', 'Сон', 'Замедление', 'Невосприимчивость к магии', 'Оглушение', 'Провокация'
                          ]
        hero_skills = []
        for i in range(random.randint(0, 3)):
            skill = random.choice(list_of_skills)
            if skill not in hero_skills:
                hero_skills.append(skill)

        return hero_skills

def Character_generator():
    hero = Character
    print("Имя:", hero.get_random_name())
    print("Возраст:", hero.get_random_age())
    print("Класс апа:", hero.get_random_class())
    print("Параметры:", hero.get_random_parameters())
    print("Характеристики:", hero.get_random_characteristics())
    print("Навыки персонажа: ", hero.get_random_skill())


if __name__ == '__main__':
    num_of_characters = int(input("Введиет количесвто персонажей для генерации: "))
    for i in range(num_of_characters):
        print(f"\n--------{i+1}-й персонаж--------")
        Character_generator()

    input()
