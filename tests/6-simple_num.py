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

for i in range(15) :
	print('Number %d is prime, ' % i, end='')
	if_prime(i)

'''
ask=input("Введите число от 0 до 1000: ")
if_prime(int(ask))
'''
