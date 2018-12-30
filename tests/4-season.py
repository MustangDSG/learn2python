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

ask=input("Введите номер месяца: ")
ask=int(ask)
season(ask)
