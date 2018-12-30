 #Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
 #и возвращающую True, если оно простое, и False - иначе.

def if_prime(num):
	if num in range(0, 1000):
		i=2
		while i < num:
			if num%i!=0:
				prime=True
				i+=1
			else:
				prime=False
				break
		print(prime)
	else:
		print("Ну по-человечески же просили ввести число в указанном диапазоне!")

ask=input("Введите число от 0 до 1000: ")
if_prime(int(ask))


