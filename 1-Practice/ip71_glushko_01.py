#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Get a name of input file
numberRead = []
numbersInt = []

pairHigh = []
unpairLow = []

finalAr = []

def sortIns(arr):
    # Сортировку выполняем, начиная с 2го элемента
    for i in range(1, len(arr)):
        # Берем элемент, который "перемещаем"
        toSort = arr[i]

        # Берем элемент, с которым сравниваем - это предыдущий в массиве
        j = i - 1

        # Если ключ меньше предыдущего элемента - сдвигаем ключ назад
        while(j > -1) and (toSort < arr[j]): #j = -1 - это когда ключ уже в самом начале
            # Меняем элементы местами
            arr[j + 1] = arr[j]
            j = j - 1

        # Иначе, возвращаем ключ на место
        arr[j + 1] = toSort

    return arr


# Считываем имя файла
fileName = raw_input('Enter the file name: ')

# Считываем элементы из файла в массив
with open(fileName) as inputFile:
    numbersRead = inputFile.readlines()
    numbersInt = [int(x) for x in numbersRead]
    print(numbersInt)

# Удаляем первый элемент, ведь это к-во элементов
numbersInt.pop(0)

# Выполняем сортировку
numbersSorted = sortIns(numbersInt)

# Разбиваем массив на парные и непарные числа, последние в спадающем порядке
for el in numbersSorted:
    if el % 2 == 0:
        pairHigh.append(el)
    else:
        unpairLow.append(el)

unpairLow = unpairLow[::-1]

# Формируем выходной массив
for el1 in pairHigh:
    finalAr.append(el1)

for el2 in unpairLow:
    finalAr.append(el2)

# Записываем результаты в файл
file = open('ip71_glushko_01_output', 'w')
for el in finalAr:
    file.write(str(el) + '\n')
