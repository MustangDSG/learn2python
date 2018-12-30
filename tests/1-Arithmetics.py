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
	

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
deis = input("Какое действие необходимо совершить?")

arithmetic(num1, num2, deis)

