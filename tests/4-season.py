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

for month in range(0, 13):
	print('Month %d is %s season.' % (month, season_alt(month)))


'''
ask=input("Введите номер месяца: ")
ask=int(ask)
season(ask)
'''