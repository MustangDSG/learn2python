import zmq 

host = '127.0.0.1'
port = 12345

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
while True:
	request_str = "message #%s" % num
	request_bytes = request_str.encode('utf-8')
	client.send(request_bytes)
	reply_bytes = client.recv()
	reply_str = reply_bytes.decode('utf-8')
	print("Sent %s, recieved %s" % (request_str, reply_str))