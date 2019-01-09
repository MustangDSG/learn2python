 #Bill Lubanovic - Introducing Python chapter 4 tasks.

divider="-------------------------------------------------------------"
print("Вывод результатов упражнений к 4 главе.")
print(divider)

#Задание 1.
'''
Присвойте значение 7 переменной guess_me. Далее напишите условные
проверки (if, else, elif), чтобы вывести строку 'too low', если 
значение переменной guess_me меньше 7, 'too high', если оно больше 7,
и 'just right', если равно 7.
'''

guess_me = 7.0				#можно сравнивать int с float
if guess_me == 7:
	print('Just right')
elif guess_me < 7:
	print('Too low')
elif guess_me > 7:
	print('Too high')
else:
	print('Something gone wrong!')
print(divider)


#Задание 2.
'''
Присвойте значение 7 переменной guess_me и значение 1 переменной start.
Напишите цикл while, который сравнивает переменные start и guess_me.
Выведите строку 'too low', если значение переменной start меньше значения
переменной guess_me. Если значение переменной start равно значению переменной
guess_me, выведите строку 'found it!' и выйдите из цикла. Если значение переменной
start больше значения переменной guess_me, выведите строку 'oops' и выйдите из цикла.
Увеличьте значение переменной start на выходе из цикла.
'''

guess_me = 7
start = 1
while start <= guess_me:
	if start < guess_me:
		print(start, 'is too low')
	elif start == guess_me:
		print(start, 'Found it!')
		break
	elif start > guess_me:
		print('oops')
		break
	start += 1
print(divider)
#Задание 3.
'''
Используйте цикл for, чтобы вывести на экран значения списка [3, 2, 1, 0]
'''

print('Вывод значений списка через цикл:')
c4_list1 = [3, 2, 1, 0]
for i in c4_list1:
	print(i)
print(divider)

#Задание 4.
'''
Используйте включение списка, чтобы создать список, который содержит нечетные числа
в диапазоне range(10).
'''

c4_list2 = list(range(1,10,2))
c4_list3 = [number for number in range(10) if number % 2 == 1]
print('Создание списка нечетных чисел:', c4_list2, c4_list3)
print(divider)

#Задание 5.
'''
Используйте включение словаря, чтобы создать словарь squares. Используйте
вызов range(10), чтобы получить ключи, и возведите их в квадрат, чтобы получить
их значения.
'''

squares = {a:a**2 for a in range(10)}
print('Итоговый словарь:', squares)
print(divider)	


#Задание 6.
'''
Используйте включение множества, чтобы создать множество odd, которое
содержит четные числа в диапазоне range(10).
'''

odd = {number for number in range(10) if number % 2 == 0}
print('Множество четных чисел:', odd)
print(divider)


#Задание 7.
'''
Используйте включение генератора, чтобы вернуть строку 'Got' и количество
чисел в диапазоне range(10). Итерируйте по нему с помощью цикла for.
'''

got = (i for i in range(10))
for j in got:
	print(j)
print(divider)
#Я не понял, что значит "Используйте включение генератора, _чтобы вернуть_ строку 'Got'",
#потому просто использовал генератор и итерировал по нему. Got в данном случае объект.

#Задание 8.
'''
Определите функцию good, которая возвращает список ['Harry', 'Ron', 'Hermione']
'''

def good():
	return ['Harry', 'Ron', 'Hermione']

print('Значения, возвращаемые функцией:', good())
print(divider)


#Задание 9.
'''
Определите функцию генератора get_odds, которая возвращает четные числа из
диапазона range(10). Используйте цикл for, чтобы найти и вывести третье
возвращенное значение.
'''

def get_odds(value):
	odds=[number for number in range(10) if number % 2 == 0]
	return odds[value]

print('Получаем третье значение из генерируемого списка:', get_odds(2))
print(divider)

#Задание 10.
'''
Определите декоратор test, который выводит строку 'start', когда вызывается
функция, и строку 'end', когда функция завершает свою работу.
'''

def test(func):
	def decorated_function():
		print('Start')
		func()
		print('End')
	return decorated_function

@test
def simple():
	print('Простая функция')

simple()
print(divider)

#Задание 11.
'''
Определите исключение, которое называется OopsException. Сгенерируйте его,
чтобы увидеть, что произойдет. Затем напишите код, позволяющий поймать это
исключение и вывести стоку 'Caught an oops'.
'''

class OopsException(Exception):
	pass

try:
	raise OopsException('panic')
except OopsException as exc:
	print('Caught an oops:', exc)
print(divider)

#Задание 12.
'''
Используйте функцию zip(), чтобы создать словарь movies, который объединяет
в пары эти списки: titles=['Creature of Habit', 'Crewel Fate'] и
plots=['A nun turns into a monster', 'A haunted yarn shop'].
'''

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
print("Объединяем списки в пары и создаем словарь:", dict(zip(titles, plots)))