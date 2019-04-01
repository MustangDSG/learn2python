import zmq
import re

mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
''' 

#параметры для запуска сервера
host = '127.0.0.1'
port = 12345

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))



#созадем список слов, начинающихся с гласной
vowels = []
for word in re.findall(r'\b[aeiouAEIOU]\w+', mammoth):
	vowels.append(word)

#созадем список слов, состоящих из 4 букв
four_letters = []
for word in re.findall(r'\b\w{4}\b', mammoth):
	four_letters.append(word)

print("Сервер запущен")

#основной цикл
while True:
	request_bytes = server.recv()
	request_str = request_bytes.decode('utf-8')
	if request_str == 'message #1':
		print("Recieved: %s" % request_str)
		i = 0
		while i <= len(vowels):
			i += 1
			reply_bytes = bytes(vowels[i], 'utf-8')
			server.send(reply_bytes)
	elif request_str == 'message #2':
		print("Recieved: %s" % request_str)
		i = 0
		while i <= len(four_letters):
			i += 1
			reply_bytes = bytes(four_letters[i], 'utf-8')
			server.send(reply_bytes)
	else:
		print("Что-то пошло не так.")