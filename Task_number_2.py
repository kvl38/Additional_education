# Задание №2

import random

def Rand_phr_gen():
    print("-----------------------------------")
    stop_word = input("Введите \"стоп слово\": ")
    noun_counter = 1
    nouns = []
    print("-----------------------------------\n"
          "Напишите существительные (по одному на строку). Если хотите перейти к вводу глаголов - напишите вместо существительного Ваше \"стоп слово\"\n\n"
          "--------Ввод существительных--------")
    noun = input(f"Введите {noun_counter}-е существительное: ")
    while noun != stop_word:
        nouns.append(noun)
        noun_counter += 1
        noun = input(f"Введите {noun_counter}-е существительное: ")

    verb_counter = 1
    verbs = []
    print("-----------------------------------\n\n"
          "Напишите глаголы (по одному на строку). Если хотите закончить ввод - напишите вместо глагола Ваше \"стоп слово\"\n\n"
          "--------Ввод глаголов--------")
    verb = input(f"Введите {verb_counter}-й глагол: ")
    while verb != stop_word:
        verbs.append(verb)
        verb_counter += 1
        verb = input(f"Введите {verb_counter}-й глагол: ")
    print("-----------------------------------")

    num_of_phrases = int(input("Введите количество наборов фраз для генерации: "))

    for i in range(num_of_phrases):
        print("==========================\n"
            f"{i+1}-й набор:")
        print(random.choice(nouns), random.choice(verbs), random.choice(nouns))
        print(random.choice(verbs), random.choice(nouns), random.choice(nouns))
        print(random.choice(nouns), random.choice(nouns), random.choice(verbs))


if __name__ == '__main__':
    Rand_phr_gen()
