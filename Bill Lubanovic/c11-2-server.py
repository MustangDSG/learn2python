from datetime import datetime
import zmq

host = '127.0.0.1'
port = 5000
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))

while True:
	request_bytes = server.recv()
	request_str = request_bytes.decode('utf-8')
	print("Recieved: %s" % request_str)
	reply_str = datetime.now().isoformat()
	reply_bytes = bytes(reply_str, 'utf-8')
	server.send(reply_bytes)
 
