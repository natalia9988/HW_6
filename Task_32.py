### Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
 
list=[randint(1, 20) for _ in range(10)]
print("Задан массив :", list, sep='\n')
min_number = int(input('Введите минимальное значение в массиве : '))
max_number = int(input('Введите максимальное значение в массиве : '))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)