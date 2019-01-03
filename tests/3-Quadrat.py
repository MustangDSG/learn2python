#Написать функцию square, принимающую 1 аргумент — сторону квадрата,
#и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
	if side <= 0:
		print('Wrong parameter.')
		return
	kortej=(side*4, side*side, side*pow(2, 0.5))
	print(kortej)
	pass

for i in range(-5, 5):
	print('Square side %d, perimeter, size, diagonal, ' % i, end = '')
	square(i)

'''
ask=input("Введите сторону квадрата: ")
ask=int(ask)
square(ask)
'''