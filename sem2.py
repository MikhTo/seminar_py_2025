# Сегодня рассмотрим стандартные коллекции list, dict, tuple и set
lst:list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print(lst)

# Со списком можно делать разное:

# Можно добавлять новые элементы:
lst.append(1)
lst.append("stroka") # Можно хранить объекты ЛЮБОГО типа
lst.append([1,2,3,5]) # Даже другие списки
print(lst)

l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]
print(l1+l2)
# Можно убрать последний элемент
last_element = lst.pop()
print(last_element)
lst.pop()

# Внимание! Плохая практика создавать список при помощи append
stupid_list = []
for i in range(0, 10):
    stupid_list.append(i) # Будет работать медлено (за счет постоянной реаллокации памяти)
# лучше использовать list comprehension (о нем далее)
print(stupid_list)

smart_list = [i for i in range(10)]
print(smart_list)

# Можно добавлять элементы, только ессли они удовлетворяют какому-то условию
smart_list = [i for i in range(10) if i%2 == 0]
print(smart_list)

# Более сложные условия можно добавлять при помощи условных выражений
smart_list = [i if i%2 == 0 else -i for i in range(10)]
print(smart_list) 

# Полезное применение: если в списке есть разные типы данных:
strange_list = [1,2,3,4,5,6,"7",8,9,10]

#Задача: хотим, чтобы в списке были одни int'ы
# 1. Можно так:
res = [i if isinstance(i, int) else int(i) for i in strange_list]
print(res)
# А можно просто всегда вызывать int -- тоже сработает
res = [int(i) for i in strange_list]
print(res)
# Давайте тепрь поговорим про срезы:
new_list = [-i for i in lst] + lst # опа, есть сложение
print(new_list)

# Срезы позволяют получить новый список, который является подмножеством исходного:
slice_1 = new_list[5:15] # Получили срез из элементов от 5 до 15 (невключительно)
print(slice_1)

# Можно задавать шаг
slice_2 = new_list[5:-5:2] # Заметьте, что можно задавать отрицательные индексы (отсчет с конца списка)
print(slice_2)
# Шаг тоже можно сделать отрицательным:
slice_3 = new_list[-5:5:-2]
print(slice_3)
# Как обратить список?
print(new_list)
print(new_list[::-1])
# tuple - кортеж - неизменяемый список
tpl = (1,2,3,4,4,3,2,1)
print(tpl[1])
#tpl[0] = -1 #--- ошибка!

# dict - словарь
# хранит пары ключ:значения
# ключи должны иметь неизменяемый тип

dct = {"first": 1, 2:"два", "list":lst, (1,1):1}
print(dct["first"])

# итерируемся по словарю
for key in dct:
    print(f"Key is {key}, value is {dct[key]}")

#можно воспользоваться функцией enumirate, чтобы получать номер каждой итерации
for i, key in enumerate(dct):
    print(f"Key is {key}, key number is {i}, value is {dct[key]}")

#есть также dict comprehension
numbers = {i:str(i) for i in range(0, 10)}


#set -- множество
#удобно, когда нужно получить уникальные значения из какого-то контенера
to_set = [1]+2*[2]+3*[3]+4*[4]
st = set(to_set)
print(st.pop())

# небольшое дополнение: c помощью in можно узнать, есть ли какой-то элемент в коллекции (любой)
print(2 in st)
print(10 in st)
print("is the Java in Java Script: ", "Yes" if "Java" in "JavaScript" else "No" )

#В прошлый раз не рассказали о сортировках: исправляемся

#сделаем список 
some_list = list(range(-7, 7, 1))
#и перемешаем его с помощью функции shuffle из библиотеки random
from random import shuffle
shuffle(some_list)

#можно либо создать новый список с помощью функции sorted 
new_list = sorted(some_list)
#либо отсортировать сам список с помощью метода sort
some_list.sort()
#сортировка в обратном порядке
some_list.sort(reverse=True)
#можно создать сортировку по более сложному критерию
#например по модулю
#для этого надо передать с аргументом key функцию, которая будет применяться к каждому элементу
def some_func(x:int):
    return abs(x)

some_list.sort(key=lambda x: abs(x))

#примерно также можно работать с функциями max и min
min_el = min(some_list)
min_el = min(some_list, key=lambda x: abs(x))

#контрольная задача: как отсортировать по четности?
print(sorted(some_list, key=lambda x: x%2))

#Строки и работа с текстом
some_string = "это какая-то строка для демонстрации работы со строками в языке Python"

some_string = some_string.replace("о", "*", 1)

print(some_string.split("-")) #разделяем по разделителю+

#в физике мы часто сталкиваемся с csv-форматом хранения чисел
#c ним можно легко справиться с помощью .split

csv_string = "1,2,3,5,7,8,9,0,10"
#хотим превратить это в список чисел

#можно через list comprehension
csv_res1 = [int(s) for s in csv_string.split(",")]

#поиск
index = some_string.find("то")
second_index = some_string.find("то", some_string.find("о"))
#подсчет вхождений
amount = some_string.count("о")
#очень полезная функция, можно создать счетчик
counter = {symb:some_string.count(symb) for symb in set(some_string)}

# строки можно складывать
str1 = "какой-то текст"
res = str1[:str1.find("то")+2] + " новый " + str1[str1.find("то")+3:]
print(res)

another_string = "\n    куча пробельных символов вокруг \n\t"
another_string = another_string.strip()

#raw-строки
raw_string = r'\n любые спец символы теперь просто символы \n\t'

#часто при описании работы r-строк говорят, что специальные символы экранируются 
#raw-строки удобно использовать при работе с файловой системой и запросах в сеть

# работа с файлами
#откываем файл
f = open(r"C:\CppPy\Materials\seminar_py\test_read.txt", "r", encoding = "utf-8") # encoding - необязательный параметр
# 'r' - чтение, 'w' - запись (старое содержимое файла стирается), 'a' - дозапись

#можно считать так:
text = f.read()

f.close()

f = open("test_read.txt", "r", encoding = "utf-8")
#А можно так:
text = []
for line in f:
    text.append(line)

f.close()

#чтобы не забывать закрыть файл можно его открыть с помощью with as
with open("test_read.txt", encoding="utf-8") as tr, open("empty_file.txt", "w", encoding="utf-8") as ef:
    text = " Очень сложно ".join(tr) #данный метод создает строку,
    #составленную из элементов контейнера, разделенных исходной строкой
    ef.write(text)
#with -- мененджер контекста 