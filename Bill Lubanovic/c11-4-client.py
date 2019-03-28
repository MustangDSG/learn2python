#Lucy
import redis, time

connection = redis.Redis()
t = 0
wait = 0.5

print('Люси собирает конфеты.')
while True:
	t = t+wait
	time.sleep(wait)
	message = connection.blpop('sweets')
	if not message:
		break
	value = message[1].decode('utf-8')
	if value == 'quit':
		break
	print('Сортировка конфет:', value)
	print('Времени потрачено: ', t, 'сек')
print('Конфеты отсортированы.')
