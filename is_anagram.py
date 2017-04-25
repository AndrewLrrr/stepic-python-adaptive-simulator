# Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.
#
# Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.
#
# Формат ввода:
#
# Два слова, каждое на отдельной строке.
# Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.
#
# Формат вывода:
# True или False.


def is_anagram(word, anagram):
    word = ''.join(sorted(word.upper()))
    anagram = ''.join(sorted(anagram.upper()))
    return word == anagram


def main():
    w1 = input()
    w2 = input()
    print(is_anagram(w1, w2))


if __name__ == '__main__':
    main()
