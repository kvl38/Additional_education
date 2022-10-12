# Задание №3

import difflib

def Word_check():
    line1 = input("Напишите “правильные” слова через пробел. Для окончания ввода нажмите Enter\n"
          "Правильные слова: ")
    right_words = line1.split()

    line2 = input("Напишите Ваш текст для проверки: ")
    text_to_check = line2.split()
    print("===================================")
    for word in text_to_check:
        for correct_word in right_words:
            if difflib.SequenceMatcher(None, word.lower(), correct_word.lower()).ratio() >= 0.6:
                for it in range(len(word)):
                    if len(word) == len(correct_word):
                        if word[it].lower() != correct_word[it].lower():
                            # original_word = text_to_check[text_to_check.index(word)]
                            print("Ошибка в слове: ", word[:it]," ",word[it]," ",word[it+1:len(word)], sep="")
                            break
    print("===================================")


if __name__ == '__main__':
    Word_check()