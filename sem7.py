#Работа с интернетом
import requests 

response = requests.get(
    "https://cpp-python-nsu.inp.nsk.su/")
#строка -- это url -- Uniform Resource Locator

# https - используемый протокол
# cpp-python-nsu.inp.nsk.su - домен - имя нашего сайта в интернете

print("Статус-код: ", response.status_code)

#1XX -- информационное сообщение (например, что запрос сервером получен, но еще не обработан)
#2XX -- успех
#3XX -- перенаправление 
#4XX -- ошибка
#5XX -- ошибка на стороне сервера

#HTML - HyperText Markup Language
#HTML - язык разметки, который говорит браузеру что и где отрисовывать
print("html code: ",  response.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text)
menu_obj = soup.find_all(class_="relative z-10")
res = [obj.text for obj in menu_obj]
print(res)


#можно вытаскивать информацию из разметки (парсить)

# однако сервер может вернуть не только html
# очень часто к серверу обращаются не люди, 
# а другие компьютеры (другие серверы, программы и т.п.)

# Некоторые web-сервисы позволяют работать с собой и без знания html
# Для этого они предоставляют API - Application Programming Interface  
# Давайте рассмотрим работу с web-сервисом через API (на лекции вам демонстрировали работу с метеосервисом) 


# работа с API идет следующим образом: 
# 1. заходим на сайт, где изучаем, какую функциональность нам предоставляет API
# 2. копируем интересующий нас запрос
# 3. некоторые API требуют регистрации и ввода пароля
# 4. Пишем нашу программу и запускаем
# 5. ???
# 6. PROFIT!

# Простые примеры не работают, поэтому будет сложный,
# зато полезный -- API Московской Биржи
mani = requests.get("http://iss.moex.com/iss/securities/SBER/dividends.json") #"?json=true" - хотим получить ответ в формате json - о нем далее

print(mani.text)
print(type(mani.text))

#по распечатанному выше примеру наглядно видно, что собой представляет json --
# -- словарь (но записанный в строку)
#ключи словаря - названия параметров
#значения могут быть разные, часто это тоже словари 
#такой формат очень удобен, так как не привязан к какому либо языку программирования (хоть и уходит корнями в JS)
#как вы заметили, json может легко воспринимать и человек

#давайте сохраним наш json-ответ в файл

#создадим json-объект, используя бибилиотеку json
import json

json_obj = json.loads(mani.text)

#параметры можно менять
print(json_obj["dividends"]["data"][0])
print(type(json_obj)) #т.о. json.loads - легкое превращение строки в словарь

#чтобы записать что-то в json используется метод dump, считать - load

with open("json_answ.txt", "w") as json_txt:
    json.dump(json_obj["dividends"]["data"], json_txt)

with open("json_answ.txt") as json_txt:
    json_from_file = json.load(json_txt)


from MyComplex import Complex

#Метод, который вызывается при создании объекта класса, называется инициализатором
c1 = Complex(1, 1)
c2 = Complex(2, 2)

#Можно создавать обычные методы
c2.conj()
print(f"abs: {c2.abs()}, phase: {c2.phase()}")
 
#А можно "магические"
#"Магические" методы определяют работу операторов/встроенных функций и т.п.
is_eq = c1 == c2
c3 = c2 + c1
try:
    c2 + "много чисел"
except ValueError:
    print("Складывай правильно!")
except Exception:
    print("Ничего не понятно, но очень грустно")
finally:
    print("Я всегда выполняюсь")

print(f"Is 1 real or imaginary part of c3? It is the {1 in c3} statement")
print(abs(c3))
#Можно сделать объект индексируемым
print(f"c3: re = {c3[0]}, img = {c3['img']}")
c3 = c1 + c2

print(c3)
print(reversed(c3))
    
#Можно сделать объект вызываемым
c3()
c3("a", "b", "v", arg1=1, arg2=2, arg3=3)

#Страшный факт: атрибуты можно добавлять прям по ходу выполнения программы
c3.wth = "idk"
print(c3.wth)
