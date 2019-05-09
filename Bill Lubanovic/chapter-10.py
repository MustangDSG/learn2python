#Bill Lubanovic - Introducing Python chapter 10 tasks.

divider="-------------------------------------------------------------"
print("Вывод результатов упражнений к 10 главе.")
print(divider)

# Задание 1.
# Запишите текущие дату и время как строку в текстовый файл today.txt.
# если написать просто 'import datetime', то скрипт будет выдавать ошибку

from datetime import datetime

with open('today.txt', 'wt') as today_file:
	current_date=str(datetime.now())
	print("1) Текущая дата, записываемая в файл:", current_date)
	today_file.write(current_date)
print(divider)

# Задание 2.
# Прочтите текстовый файл today.txt и разместите данные в строке today_string.

with open('today.txt', 'rt') as today_file:
	today_string = today_file.read()
	print("2) Дата из файла:", today_string)
print(divider)

# Задание 3.
# Разберите дату из строки today_string.

get_date = datetime.strptime(today_string, '%Y-%m-%d %H:%M:%S.%f')
print("3) Преобразуем строку в дату по шаблону: ", get_date)
print(divider)

# Задание 4.
# Выведите на экран список файлов текущего каталога.

import os

print("4) Вывод списка файлов и папок текущего каталога:")
print("Текущий каталог:", os.getcwd())

# Далее 2 варианта вывода информации:
# Первый, вывод через запятую сплошной строкой:
# print("Содержимое каталога:\n", os.listdir(path='.'))
# Второй, построчным списком (занимает много вертикального пространства):

for item in os.listdir(path='.'):
	print(item)
print(divider)

# Задание 5.
# Выведите на экран список файлов родительского каталога.

print("5) Вывод списка файлов и папок родительского каталога:")
print(os.listdir(path='..'))

# Примечание: в консоли sublime-text в выводе показываются файлы и папки
# родительского каталога, как и ожидается, а вот в консоли linux-а, уже на уровень выше.
# Модуль os работает в разных средах по разному и по уму-то нужно
# писать сначала проверку на тип системы и отдельные куски кода под
# конкретный вариант.

print(divider)

# Задание 6.
# Используйте модуль multiprocessing, чтобы создать три отдельных процесса.
# Заставьте каждый из них ждать случайное количество секунд (от одной до пяти),
# вывести текущее время и завершить работу.

import multiprocessing, time, random

def count():
	time.sleep(random.randint(1, 2))
	print("Counter:", datetime.now(), '\n')
	#вывод потоков будет в самом конце консоли

print("6) Вывод через multiprocessing:")

if __name__ == '__main__':
	for i in range(3):
		proc = multiprocessing.Process(target=count)
		proc.start()
		time.sleep(10)
		proc.terminate()

print(divider)

# Задание 7.
# Создайте объект date, содержащий дату вашего рождения.

from datetime import date

birthday = date(1956, 1, 31)
print("7) Дата рождения Гвидо Ван Россума:", birthday)
print(divider)

# Задание 8.
# В какой день недели вы родились?

import calendar
from datetime import timedelta

print("8) День рождения Гвидо Ван Россума:",calendar.day_name[birthday.weekday()])
print(divider)

# Задание 9.
# Когда вам будет (или уже было) 10 000 дней от роду?

inc_days = birthday + timedelta(days=10000)
print("9) День, когда Гвидо Ван Россуму будет 10 000 дней от роду:", inc_days)

