#Bill Lubanovic - Introducing Python chapter 7 tasks.

divider = "-----------------------------------";
print("Вывод результатов упражнений к 7 главе.")
print(divider)

#Задание №1
# Создайте строку Unicode с именем mystery и присвойте ей значение '\U0001f4a9' .
# Выведите на экран значение строки mystery . Найдите имя Unicode для mystery .

import unicodedata
mystery = '\U0001f4a9'
print(mystery)
print("Имя символа в юникоде:", unicodedata.name(mystery))
print(divider)

#Задание №2
# Закодируйте строку mystery , в этот раз с использованием кодировки UTF-8,
# в переменную типа bytes с именем pop_bytes . Выведите на экран значение пере-
# менной pop_bytes.

mystery_encoded = mystery.encode('utf-8')
pop_bytes = bytes(mystery_encoded)
print("Вывод перекодированной строки в bytes:", pop_bytes)
print(divider)

#Задание №3
# Используя кодировку UTF-8, декодируйте переменную pop_bytes в строку
# pop_string . Выведите на экран значение переменной pop_string . Равно ли оно
# значению переменной mystery ?
pop_string = pop_bytes.decode('utf-8')
print("Вывод декодированной из bytes в utf-8 строки:", pop_string)
print(divider)

#Задание №4
# Запишите следующее стихотворение с помощью старого стиля форматирования.
# Подставьте строки 'roast beef' , 'ham' , 'head' и 'clam' в эту строку:
# My kitty cat likes %s,
# My kitty cat likes %s,
# My kitty cat fell on his %s
# And now thinks he's a %s.
print('''
	My kitty cat likes %s,
	My kitty cat likes %s,
	My kitty cat fell on his %s
	And now thinks he's a %s.''' % ('roast beef', 'ham', 'head', 'clam'))
print(divider)

#Задание №5
# Запишите следующее письмо по форме с помощью форматирования нового
# стиля. Сохраните строку под именем letter (это имя вы используете в следующем упражнении):
letter = '''
Dear {0[salutation]} {0[name]},
Thank you for your letter. We are sorry that our {0[product]} was {0[verbed]} in your
{0[room]}. Please note that it should never be used in a {0[room]}, especially
near any {0[animals]}.
Send us your receipt and {0[amount]} for shipping and handling. We will send
you another {0[product]} that, in our tests, is {0[percent]} less likely to
have {0[verbed]}.
Thank you for your support.
Sincerely,
{0[spokesman]}
{0[job_title]}
'''

#Задание №6.
# Создайте словарь с именем response , имеющий значения для строковых ключей
# 'salutation' , 'name' , 'product' , 'verbed' (прошедшее время от глагола verb), 'room' ,
# 'animals' , 'amount' , 'percent' , 'spokesman' и 'job_title' . Выведите на экран значение
# переменной letter , в которую подставлены значения из словаря response

response = {'salutation' : 'Mr',
			'name' : 'Lubanovic',
			'product' : 'book',
			'verbed' : 'torn',
			'room' : 'parrot cage',
			'animals' : 'funny dreamy cats',
			'amount' : 'over 9000$',
			'percent' : '73,29%',
			'spokesman' : 'Mrs. Talkalot',
			'job_title' : 'Talk manager'}
print (letter.format(response))
print(divider)

#Задание №7.
# При работе с текстом вам могут пригодиться регулярные выражения. Мы вос-
# пользуемся ими несколькими способами в следующем примере текста. Перед
# вами стихотворение Ode on the Mammoth Cheese, написанное Джеймсом Макин-
# тайром (James McIntyre) в 1866 году во славу головки сыра весом 7000 фунтов,
# которая была сделана в Онтарио и отправлена в международное путешествие.
# Если не хотите вводить это стихотворение целиком, используйте свой любимый
# поисковик и скопируйте его текст в программу. Или скопируйте его из проекта
# «Гутенберг» ( http://bit.ly/mcintyre-poetry ). Назовите следующую строку mammoth :

mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

#Задание №8.
# Импортируйте модуль re , чтобы использовать функции регулярных выражений
# в Python. Используйте функцию re.findall() , чтобы вывести на экран все слова, которые начинаются с буквы «с».

import re
print("Слова, которые начинаются с буквы «с»:")
print(re.findall(r'c\w+', mammoth))
print(divider)

#Задание №9. 
# Найдите все четырехбуквенные слова, которые начинаются с буквы «c».

print("Четырехбуквенные слова, которые начинаются с буквы «c»:")
print(re.findall(r'c\w{3}\b', mammoth))
print(divider)

#Задание №10.
# Найдите все слова, которые заканчиваются на букву «r».

print("Слова, которые заканчиваются на букву «r»:")
print(re.findall(r'\w+r\b', mammoth))
print(divider)

#Я не сразу понял, что порядок "операторов" регулярных выражений имеет значение.
#Если в этом задании выражение заменить на r'\b\w+r'
#результат будет близкий, но не совсем тот, который требуется.

#Задание №11.
#Найдите все слова, которые содержат три гласные подряд.

print("Слова, которые содержат три гласные подряд:")
print(re.findall(r'\b\w+[aeiouAEIOU]{3}\w+', mammoth))
print(divider)

#Задание №12.
# Используйте метод unhexlify для того, чтобы преобразовать шестнадцатеричную
# строку, созданную путем объединения двух строк, что позволило ей разместить-
# ся на странице, в переменную типа bytes с именем gif :
# '47494638396101000100800000000000ffffff21f9' +
# '0401000000002c000000000100010000020144003b'

import binascii

hex_var = '47494638396101000100800000000000ffffff21f9' + \
		  '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_var)

#Задание №13.
# Байты, содержащиеся в переменной gif , определяют однопиксельный прозрач-
# ный GIF-файл. Этот формат является одним из самых распространенных.
# Корректный файл формата GIF начинается со строки GIF89a . Является ли этот
# файл корректным?

print(gif)

#Мощнейшее задание. Как видим из вывода принта - файл является корректным.

#Задание №14. 
# Ширина файла формата GIF является шестнадцатибитным целым числом с об-
# ратным порядком байтов, которое начинается со смещения 6 байт. Его высота
# имеет такой же размер и начинается со смещения 8 байт. Извлеките и выведите
# на экран эти значения для переменной gif . Равны ли они 1?

import struct

width, height = struct.unpack('<HH', gif[6:10])
print("Размеры gif-файла:", width, height)

#Оба значения равны 1
