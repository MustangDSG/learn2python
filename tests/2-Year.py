#Написать функцию is_year_leap, принимающую 1 аргумент — год,
#и возвращающую True, если год високосный, и False иначе. 

def is_year_leap (check):
	if (check % 4 == 0 and check % 100 != 0) or check % 400 == 0:
		return True
	else:
		return False

print('Year is %d,' % 2019, is_year_leap(2019))
print('Year is %d,' % 2020, is_year_leap(2020))
print('Year is %d,' % 2000, is_year_leap(2000))
print('Year is %d,' % 1900, is_year_leap(1900))

#is_year_leap(int(input("Введите число года для проверки: "))) #для разнообразия все в одну кучу
