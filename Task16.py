# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

def examinationType (word):
    while type(word) != int:
        try:
            word = int(word)
        except ValueError:
            print ("Ошибка. Введено не целое число")
            word = input("Повтори попытку: ")
    return word

size = input("Введите размер массива: ")
size = examinationType(size)

number = input ("Введите число для поиска: ")
number = examinationType(number)

massive=[]

for i in range(size):
    massive.append(randint(0,10))

print (massive)

count = 0

for i in range(len(massive)):
    if massive[i] == number:
        count += 1

print ("В списке число {0} встретилось {1} раз" .format(number, count))