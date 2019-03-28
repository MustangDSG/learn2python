import redis

connection = redis.Redis()

print('Simulation start.')
sweets = ['рачки', 'гусинные лапки', 'барбарис', 'василек', 'ромашка', 'ласточка']
for item in sweets:
	message = item.encode('utf-8')
	connection.rpush('sweets', message)
connection.rpush('sweets', 'quit')
print('Simulation end.')