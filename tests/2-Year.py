#Написать функцию is_year_leap, принимающую 1 аргумент — год,
#и возвращающую True, если год високосный, и False иначе. 

def is_year_leap (check):
	if check % 4 == 0:
		print(True)
	else:
		print(False)

is_year_leap(int(input("Введите число года для проверки: "))) #для разнообразия все в одну кучу
