#Bill Lubanovic - Introducing Python chapter 8 tasks.

# Вещание 8-1. Практическая часть по работе с файлами.

divider="-------------------------------------------------------------"
print("Вывод результатов упражнений к 8 главе.")
print(divider)

# Задание 1.
# Присвойте строку 'This is a test of the emergency text system' переменной test1
# и запишите переменную test1 в файл с именем test.txt.

test1 = 'This is a test of the emergency text system'
test_file = open('test.txt', 'wt')
test_file.write(test1)
test_file.close()

# Задание 2.
# Откройте файл test.txt и считайте его содержимое в строку test2. Совпадают
# ли строки test1 и test2?

with open('test.txt', 'rt') as test_file2:
	lines = test_file2.readlines()
print(lines)
print(divider)

# Задание 3.
# Сохраните следующие несколько строк в файл books.csv. Обратите внимание
# на то, что, если поля разделены запятыми, вам нужно заключить поле в кавычки,
# если оно содержит запятую:
# author,book
# J R R Tolkien,The Hobbit
# Lynne Truss,"Eats, Shoots & Leaves"

import csv

books_dict = [
			{'author' : 'JRR Tolkien', 'book' : 'The Hobbit'},
			{'author' : 'Lynne Truss', 'book' : 'Eats, Shoots & Leaves'},
			]
with open('books.csv', 'wt') as file_output:
	cout = csv.DictWriter(file_output, ['author', 'book'])
	cout.writeheader()
	cout.writerows(books_dict)

# Задание 4.
# Используйте модуль csv и его метод DictReader, чтобы считать содержимое фай-
# ла books.csv в переменную books. Выведите на экран значения переменной books.
# Обработал ли метод DictReader кавычки и запятые в заголовке второй книги?

with open('books.csv', 'rt') as file_input:
	cin = csv.DictReader(file_input)
	books = [row for row in cin]

print (books)
print(divider)

# Задание 5.
# Создайте CSV-файл books.csv и запишите его в следующие строки:
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992

books_dict2 = [
			{'title' : 'The Weirdstone of Brisingamen', 'author' : 'Alan Garner', 'year' : '1960'},
			{'title' : 'Perdido Street Station', 'author' : 'China Miéville', 'year' : '2000'},
			{'title' : 'Thud!', 'author' : 'Terry Pratchett', 'year' : '2005'},
			{'title' : 'The Spellman Files', 'author' : 'Lisa Lutz', 'year' : '2007'},
			{'title' : 'Small Gods', 'author' : 'Terry Pratchett', 'year' : '1992'},
			]

with open('books2.csv', 'wt') as file_output:
	cout = csv.DictWriter(file_output, ['title', 'author', 'year'])
	cout.writeheader()
	cout.writerows(books_dict2)

# Вещание 8-2. Работа с БД. Практическая часть.

# Задание 6.
# Используйте модуль sqlite3, чтобы создать базу данных SQLite books.db и таб­-
# лицу books, содержащую следующие поля: title (text), author (text) и year
# (integer).

import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute("""DROP TABLE IF EXISTS books""")  
#эта строчка нужна, чтоб не удалять каждый раз таблицу вручную, т.к. с первого раза у меня не получается все сделать верно
curs.execute("""CREATE TABLE IF NOT EXISTS books (
	title TEXT,
	author TEXT,
	year INTEGER
	) """)

# Задание 7.
# Считайте данные из файла books.csv и добавьте их в таблицу book.

with open('books2.csv', 'rt') as file_input2:
	cin2 = csv.DictReader(file_input2)
	values_to_base = [(i['title'], i['author'], i['year']) for i in cin2]

curs.executemany("INSERT INTO books VALUES (?,?,?)", values_to_base)
#В учебнике про следующую строчку ни слова, а без нее запись в базу не произойдет.
conn.commit()

# Задание 8.
# Считайте и выведите на экран графу title таблицы book в алфавитном порядке.

print("Вывод данных из таблицы по графе title в алфавитном порядке:")
curs.execute('SELECT title FROM books ORDER BY title ASC')
print(curs.fetchall())
print(divider)

# Задание 9.
# Считайте и выведите на экран все графы таблицы book в порядке публикации.

print("Вывод данных из таблицы по всем графам в порядке публикации:")
curs.execute('SELECT * FROM books ORDER BY year ASC')
print(curs.fetchall())
print(divider)

# Задание 10.
# Используйте модуль sqlalchemy, чтобы подключиться к базе данных sqlite3
# books.db, которую вы создали в упражнении 6. Как и в упражнении 8, считайте
# и выведите на экран графу title таблицы book в алфавитном порядке.

import sqlalchemy as sa

conn2 = sa.create_engine('sqlite:///books.db')
titles_from_base = conn2.execute('SELECT title FROM books ORDER BY title ASC')
print("Вывод через просто print покажет объект:", titles_from_base)
print("Для вывода всех значений нужен итератор:", end=' ')
for rows in titles_from_base:
	print(rows, end=' ')
print(divider)

# Задание 11.
# Установите сервер Redis и библиотеку Python redis (с помощью команды pip
# install redis) на свой компьютер. Создайте хеш redis с именем test , содержащий
# поля count (1) и name ('Fester Bestertester'). Выведите все поля хеша test.

# Примечание:
# Нужно еще и сам redis сервер установить, иначе интерпретатор
# будет ругаться на невозможность подключения.

import redis

conn3 = redis.Redis('localhost')
conn3.hmset('test', {'count' : '1', 'name' : 'Fester Bestertester'})
print("Вывод хэша Redis:", conn3.hmget('test', 'count', 'name'))
print(divider)

# Задание 12.
# Увеличьте поле count хеша test и выведите его на экран.

conn3.mset({"counter": "1", "name": "Fester"})
conn3.incr("counter")
print("All values hash Redis:", conn3.mget(["counter", "name"]))

# Примечание:
# Забавно то, что написано "увеличьте", хотя в учебнике указано только то, что
# значения хэша могут содержать только строки. Тогда либо нужно прописать
# отдельно перевод 1 из строку в инт, увеличение на некоторое число, а потом
# перевести обратно в строку и вписать в хэш. Либо сделать просто вручную.

# Финальная часть.
curs.close()
conn.close()


