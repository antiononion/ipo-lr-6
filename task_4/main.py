v = input("Введите строку для поиска: ")
file = open('text.txt', 'r', encoding='utf-8')
f_l=[]
for line in file:
    line = line.strip()
    if v in line:
        f_l.append(line)
file.close()
count = len(f_l)
print("Найдено строк, содержащих " ,v, " : " , count)

f_l_s = sorted(f_l, key=len)
    
print("Найденные строки (отсортированные по длине):")
for line in f_l_s:
    print(line)