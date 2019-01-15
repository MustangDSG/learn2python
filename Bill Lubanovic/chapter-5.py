 #Bill Lubanovic - Introducing Python chapter 5 tasks.

# Вещание 5. Модули и пакеты. Практическая часть.
divider="-------------------------------------------------------------"
print("Вывод результатов упражнений к 5 главе.")
print(divider)
# Задание 1.
# Создайте файл, который называется zoo.py В нем объявите функцию hours(),
#которая выводит на экран строку 'Open 9-5 daily.' Далее используйте
#интерактивный интерпретатор, чтобы импортировать модуль zoo и вызвать его
#функцию hours().
print('Импорт из файла.')
import zoo
zoo.hours()
print(divider)
#Задание 2.
# В интерактивном интерпретаторе импортируйте модуль zoo под именем menagerie
#и вызовите его функцию hours()
print('Импорт из файла c переименовкой.')
import zoo as menagerie
menagerie.hours()
print(divider)
# Задание 3.
# Оставаясь в интерпретаторе, импортируйте непосредственно функцию hours() из
#модуля zoo и вызовите ее.
print('Импорт конкретной функции.')
from zoo import hours
hours()
print(divider)
# Задание 4.
# Импортируйте функцию hours() под именем info и вызовите ее.
print('Импорт конкретной функции c переименовкой.')
from zoo import hours as info
info()
print(divider)
# Задание 5.
# Создайте словарь с именем plain, содержащий пары ключ-значение 'a':1, 'b':2, 'c':3,
#а затем выведите его на экран
plain={"c" : 5, "a" : 4, "b" : 3,}
plain["d"] = 7; plain["ab"] = 8
plain.update({"a" : 9})
print('Простой словарь.', plain)
print(divider)
# Задание 6.
# Создайте OrderedDict с именем fancy из пар ключ-значение, приведенных в задании 5,
#и выведите его на экран. Изменился ли порядок ключей?
from collections import OrderedDict
fancy=OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy2=OrderedDict(plain)
print('Упорядоченный словарь.', fancy, fancy2)
print(divider)
# Задание 7.
# Создайте defaultdict с именем dict_of_lists и передайте ему аргумент list.
# Создайте список dict_of_lists['a'] и присоедините к нему значение
#'something for a' за одну операцию. Выведите на экран dict_of_lists['a'].
from collections import defaultdict
dict_of_lists=defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists)
