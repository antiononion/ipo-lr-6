# Милашевский 88 тп
#Запрашиваем у пользователя число строк
n = int(input("Введите число строк: "))
#Читаем строки
lines = []
for i in range(n):
    lines.append(input())
#Собираем все слова
text = ' '.join(lines)
words = text.split()
#Находим количество уникальных слов
unique_words = set(words)
#Выводим результат
print("Количество уникальных слов:", len(unique_words)) 
