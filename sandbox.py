#Написать функцию arithmetic, принимающую 3 аргумента:
#первые 2 - числа, третий - операция, которая должна быть произведена над ними.
#Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic (num1, num2, deis):
	num1=int(num1)
	num2=int(num2)
	if deis == "+":
		print(num1+num2)
	elif deis == "-":
		print(num1-num2)
	elif deis == "*":
		print(num1*num2)
	elif deis == "/":
		print(num1/num2)
	else:
		print("Неизвестная операция.")
		pass

#Написать функцию is_year_leap, принимающую 1 аргумент — год,
#и возвращающую True, если год високосный, и False иначе. 

def is_year_leap (check):
	if (check % 4 == 0 and check % 100 != 0) or check % 400 == 0:
		return True
	else:
		return False

#Написать функцию square, принимающую 1 аргумент — сторону квадрата,
#и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
	if side <= 0:
		print('Wrong parameter.')
		return
	kortej=(side*4, side*side, side*pow(2, 0.5))
	print(kortej)
	pass

#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
#и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень). 

def season (month):
	if month in range(1, 2):
		print("Зима.")
	elif month == 12:
		print("Зима.")
	elif month in range (3, 6):
		print("Весна.")
	elif month in range (6, 9):
		print("Лето.")
	elif month in range (9, 12):
		print("Осень.")
	else:
		print("Недопустимое значение") #А почему бы и да?

def season_alt(month) :
	if month not in range(1, 13) :
		print('Month not correct, must be 1..12.')
		return
	seasons = ('Winter', 'Spring', 'Summer', 'Fall' )
	monthsInYear = 12; monthsInSeason = 3
	return seasons[(month % monthsInYear) // monthsInSeason]

#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
#(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя. 

def bank (a, years):
	i=1
	while i <=years:
		a=a*1.1
		i += 1
	print (a)

def fibonacci(n):
	F0 = 0; F1 = 1; Fn = F0 + F1
	for i in range(2, n) : 
		F0 = F1; F1 = Fn; Fn = F1 + F0
	return Fn

 #Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
 #и возвращающую True, если оно простое, и False - иначе.

def if_prime(num):
	if num not in range(2, 1000):
		print("Ну по-человечески же просили ввести число в указанном диапазоне!")
		return
	i=2; prime=True
	while i < num:
		if num%i!=0:
			i+=1
		else:
			prime=False
			break
	print(prime)

#Тесты...

num1 = 3; num2 = 2; deis = 'k'

'''
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
deis = input("Какое действие необходимо совершить?")
'''
arithmetic(3, 2, '+')

#Високосный год.

print('')
print('Year is %d,' % 2019, is_year_leap(2019))
print('Year is %d,' % 2020, is_year_leap(2020))
print('Year is %d,' % 2000, is_year_leap(2000))
print('Year is %d,' % 1900, is_year_leap(1900))

#is_year_leap(int(input("Введите число года для проверки: "))) #для разнообразия все в одну кучу

print('')
for i in range(-5, 5):
	print('Square side %d, perimeter, size, diagonal, ' % i, end = '')
	square(i)
'''
ask=input("Введите сторону квадрата: ")
ask=int(ask)
square(ask)
'''

print('')
for month in range(0, 13):
	print('Month %d is %s season.' % (month, season_alt(month)))
'''
ask=input("Введите номер месяца: ")
ask=int(ask)
season(ask)
'''
print('')
print('Fibonacci:', end='')
for i in range(10):
	print('%d' % fibonacci(i), end=' ')

'''
ask_a=input("Какую сумму вкладываем? ")
ask_years=input("На какой срок? ")
bank(int(ask_a), int(ask_years))
'''
print('')
for i in range(15) :
	print('Number %d is prime, ' % i, end='')
	if_prime(i)

'''
ask=input("Введите число от 0 до 1000: ")
if_prime(int(ask))
'''

#Bill Lubanovic - Introducing Python chapter 3 tasks.

divider="-------------------------------------------------------------"
print("Вывод результатов упражнений к 3 главе.")
print(divider)
#Задание 1.
#Создайте список years_list, содержащий год, в который вы родились,
#и каждый последующий год вплоть до вашего пятого дня рождения.
years_list=['1985']
i=1
while i<=5:
	add_year=str(int(years_list[0])+i)
	years_list.append(add_year)
	i+=1
print(years_list)

#Задание 2.
#В какой из годов, содержащихся в списке years_list,
#был ваш третий день рождения?
third_birthday=years_list[3]
print("Третий день рождения был в", third_birthday, "году.")


#Задание 3.
#В какой из годов, перечисленных в списке years_list,
#вам было больше всего лет?
max_age=years_list[-1]
print("Из списка годов больше всего лет мне было в", max_age, "году.")
print(divider)

#Задание 4.
#Создайте список things, содержащий три элемента:
#"mozzarela", "cinderella", "salmonella"
things=['mozzarela', 'cinderella', 'salmonella']

#Задание 5.
#Напишите с большой буквы тот элемент списка things, который
#относится к человеку, а затем выведете список.
things[1].capitalize()
print('Изменится ли значение, при таком варианте?\n', things, '\nКак видим - не изменилось.')
things[1]=things[1].capitalize()
print('Оно изменится в списке в том случае, если мы сделаем присваивание нового значения элементу списка:\n', things)

#Задание 6.
#Переведите сырный элемент списка things в верхний регистр целиком и выведете список.
things[0]=things[0].upper()
print("Сыр теперь капсом", things)

#Задание 7.
#Удалите болезнь из списка things, получите Нобелевскую премию
#и затем выведите список на экран.
things.pop()
win_Nobel_prize=True
print("Болезни больше нет: ", things)
if win_Nobel_prize:
	print("И за это мы получили Нобелевскую премию!")
print(divider)

#Задание 8.
#Создайте список, который называется surprise и содержит элементы 'Groucho', 'Chico', 'Harpo'.
surprise=['Groucho', 'Chico', 'Harpo']

#Задание 9.
#Напишите последний элемент списка surprise со строчной буквы, затем обратите его и напишите с прописной буквы.
name_from_surprise_list=surprise[-1].lower()
print("Последний элемент строчными буквами:", name_from_surprise_list)
inverted_name=name_from_surprise_list[::-1].capitalize()
print("Обратили имя и написали с заглавной буквы:", inverted_name)
print(divider)

#Задание 10.
#Создайте англо-французский словарь, который называется e2f,
#и выведите его на экран.
e2f={"dog" : "chien", "cat" : "chat", "walrus" : "morse"}

#Задание 11.
#Используя словарь e2f, выведите французский вариант слова walrus.
print("Французский вариант слова walrus:", e2f.get("walrus"))

#Задание 12.
#Создайте французско-анлийский словарь f2e на основе словаря e2f. Используйте метод items.
f2e={v:k for k,v in e2f.items()}
print("Французско-анлийский словарь:")
print(f2e)

#Задание 13.
#Используя словарь f2e, выведите английский вариант слова chien.
print("Английский вариант слова chien:", f2e.get("chien"))

#Задание 14.
#Создайте и выведите на экран множество английских слов из ключей словаря e2f.
print("Множество из словаря e2f:", set(e2f))
print(divider)

#Задание 15.
#Создайте многоуровневый словарь life. Используйте следующие строки для
#ключей верхнего уровня: 'animals', 'plants' и 'other'.
#Сделайте так, чтобы ключ 'animals' ссылался на другой словарь, имеющий
#ключи 'cats', 'octopi' и 'emus'. Сделайте так, чтобы ключ 'cats'
#ссылался на список строк со значениями 'Henri', 'Grumpy' и 'Lucy'.
#Остальные ключи должны ссылаться на пустые словари.
cats_list=['Henri', 'Grumpy', 'Lucy']

animals_dict={
	"cats" : cats_list,
	"octopi" : "",
	"emus" : "",
}

life={
	"animals" : animals_dict,
	"plants" : "",
	"other" : "",
}

#Задание 16.
#Выведите на экран высокоуровневые ключи словаря life.
print("Высокоуровневые ключи словаря life:", life.keys())

#Задание 17.
#Выведите на экран ключи life['animals']
print("Ключи словаря life['animals']:", life['animals'].keys())

#Задание 18.
#Выведите значения life['animals']['cats']
print("Ключи словаря life['animals']['cats']:", life['animals']['cats'])
print(divider)
