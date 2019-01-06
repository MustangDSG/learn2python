#Sieve of Eratosthenes 
#Решето Эратосфена

#предел работы скрипта
limit=1000+1

#будем считать, что каждый индекс списка является простым числом
numbers_list=[True]*limit
#и сразу отбросим ноль с единицей 
numbers_list[0]=False
numbers_list[1]=False

#просеиваем все числа от 2 до 1000 включительно
for number in range(2, limit):
	if numbers_list[number]:
		for i in range(2*number, limit, number):
			numbers_list[i]=False

#создаем список только из простых чисел
prime_numbers=[]
for number in range(limit):
	if numbers_list[number]:
		prime_numbers.append(number)

print(prime_numbers)

