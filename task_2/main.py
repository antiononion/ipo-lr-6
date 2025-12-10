# Милашевский 88 тп
import random
#CОЗДАЕМ РАНДОМНЫЕ ЗНАЧЕНИЯ ДЛЯ ВЫСОТЫ И ШИРИНЫ МАТРИЦЫ
h = random.randint(4,8)
w = random.randint(4,8)
summ = 0 
#CОЗДАЕМ СПИСОК С ЧИСЛАМИ
lizt = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
#СОЗДАЕМ МАТРИЦУ ГДЕ ВЫБИРАЕТСЯ СЛУЧАЙНОЕ ЗНАЧЕНИЕ ИЗ СПИСКА
matrix  = [
#ЗНАЧЕНИЯ ВЫСОТЫ И ШИРИНЫ БЕРУТСЯ С W И H
[random.choice(lizt) for i in range(w)] 
for i in range(h)]
#ВЫВОДИМ МАТРИЦУ С ПОМОЩЬЮ ФОРМАТИРОВАННЫЙ СТРОКИ И ОТСТУПА
for row in matrix:
    print(row)
#CОЗДАЕМ УСЛОВИЕ ДЛЯ СУММЫ И ВЫВОДИМ ЕЕ
for row in matrix:
    for elem in row:
        if elem % 2 == 0:
            summ += elem
print(summ,' = сумма четных элементов') 
