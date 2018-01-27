"""
Суть задачи та же, что и Caesar cipher, с одним отличием: кодируются символы из интервала 1F600—1F64F таблицы символов 
Юникода. Используется кодировка UTF-8.

Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный 
сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу 
вправо. На второй строке указывается непустая фраза для шифрования. 

Не обращайте внимания, если у вас отображаются прямоугольники вместо некоторых символов. Это значит, что ваш шрифт не 
содержит этих символов. Для решения задачи это не имеет никакого значения.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри кавычек записана 
зашифрованная последовательность.

Sample Input 1:
1
😀🙏😇

Sample Output 1:
Result: "😁😀😈"

Sample Input 2:
1
😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿
🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏

Sample Output 2:
Result: "😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻
😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏😀"
"""

BOTTOM_LIMIT = 0x1f600
TOP_LIMIT = 0x1f64f
UNICODE_RANGE = TOP_LIMIT - BOTTOM_LIMIT + 1


def unicode_caesar_cipher(sequence, shift):
    return ''.join(chr(BOTTOM_LIMIT + (ord(x) - BOTTOM_LIMIT + shift) % UNICODE_RANGE) for x in sequence)


if __name__ == '__main__':
    s = int(input())
    e = input()
    print('Result: "{}"'.format(unicode_caesar_cipher(e, s)))


# UNICODE_RANGE = [int('1F6{}{}'.format(n, e), 16) for n in range(5) for e in list('0123456789ABCDEF')]
#
#
# def unicode_caesar_cipher(sequence, shift):
#     shift = shift % len(UNICODE_RANGE)
#     dec_sequence = [ord(c) for c in sequence]
#     encoded = []
#     for code in dec_sequence:
#         searched_index = UNICODE_RANGE.index(code) + shift
#         if searched_index >= len(UNICODE_RANGE):
#             searched_index = searched_index - len(UNICODE_RANGE)
#         encoded.append(UNICODE_RANGE[searched_index])
#     return ''.join(chr(i) for i in encoded)
