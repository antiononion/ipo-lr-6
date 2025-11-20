import random
p = []
g = 0
t = 0
k = 0
d = -99999
l = 999999
#ГЕНЕРИРУЕМ 25 ЭЛЕМЕНТОВ
for i in range(25):
    p.append(random.randint(-50,50))
print(p)
#ПРОВЕРКА НА ПОЛОЖИТЕЛЬНОСТЬ И ОТРИЦАТЕЛЬНОСТЬ
for o in p:
    if o>0:
        g+=1
    elif o<0:
        t+=1
    else:
        k+=1
#ВЫСЧИТЫВАЕМ ПРОЦЕНТЫ 
procentpol = g/(g+t+k)*100
procentotr = t/(g+t+k)*100
procentpnull = k/(g+t+k)*100
#МАКС ЧИСЛО
for x in p:
    if x>d:
        d = x
#МИН ЧИСЛО
for y in p:
    if y<l:
        l = y

#ВЫВОДИМ ПОЛУЧЕНЫЕ РЕЗУЛЬТАТЫ
print("Количество положительных элементов = ", g)
print("Количество отрицательных элементов = ", t)
print("Количество элементов равных нулю = ", k)
print("Минимальное число = ", l)
print("Максимальное число = ", d)
print("Процент положительных = ", procentpol, " Процент отрицательных = ", procentotr, " Процент нулевых = ", procentpnull)