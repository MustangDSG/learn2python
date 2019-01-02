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

print('Fibonacci:', end='')
for i in range(10):
	print('%d' % fibonacci(i), end=' ')

'''
ask_a=input("Какую сумму вкладываем? ")
ask_years=input("На какой срок? ")
bank(int(ask_a), int(ask_years))
'''