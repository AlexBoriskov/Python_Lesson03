# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

from random import randint

def examinationType (word):
    while type(word) != int:
        try:
            word = int(word)
        except ValueError:
            print ("Ошибка")
            word = input ("Введите повторно: ")
    return word

size = input ("Введите размер списка: ")
size = examinationType(size)

number = input ("Введите число для поиска: ")
number = examinationType(number)

spisok = []

for i in range(size):
    spisok.append(randint(0,10))

print (spisok)

minRaz = abs(number - spisok[0])
position = 0

for i in range(len(spisok)):
    difference = abs(number - spisok[i])
    if difference<minRaz:
        minRaz=difference
        position = i

print ("Число ближайшее к {1} равно {2}" .format(number, spisok[position]))

