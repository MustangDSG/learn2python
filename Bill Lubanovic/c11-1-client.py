import socket
from datetime import datetime

server_address = ('localhost', 5000)
max_size = 4096
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'What time is it?', server_address)
data, server = client.recvfrom(max_size)
print('Ответ от сервера:', data.decode('utf-8'))
client.close()
