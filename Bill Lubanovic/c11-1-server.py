from datetime import datetime
import socket

server_address = ('localhost', 5000)
max_size = 4096
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)
data, client = server.recvfrom(max_size)
print('Полученный запрос:', data)
sendtext=bytes(datetime.now().isoformat(), encoding = 'utf-8')
server.sendto(sendtext, client)
server.close()
