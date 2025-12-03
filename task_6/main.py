import random
сounto = 0
#СОЗДАЕМ СПИСОК ИЗ РАНДОМНЫХ ЧИСЕЛ
lisst = [[random.randint(-10, 10) for i in range(4)] for i in range(20)]
print("Исходный список из ", len(lisst), " элементов")
#ВЫВОДИМ СПИСОК
for tough in lisst:
    print(tough)
#СОЗДАЕМ КОРТЕЖ ГДЕ ТОЛЬКО УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
tupler = set()
for tough in lisst:
#СОРТИРУЕМ И ДОБАВЛЯЕМ КОМБИНАЦИИ УНИКАЛЬНЫХ ЗНАЧЕНИЙ
    sorte = tuple(sorted(tough))
    tupler.add(sorte)
ucl = list(tupler)
leng = len(ucl)
print ("Количество уникальные комбинации = ", len(ucl))
for tough in ucl:
    print(tough)
num = int(input("Введите любое число = "))
for i in range(leng):
    for j in range(i+1,leng):
        t1 = ucl[i]
        t2 = ucl[j]
total = sum(t1) + sum(t2)
if total < num:
   сounto += 1 
print("Кол-во пар меньше вписанного числа = ", сounto)
