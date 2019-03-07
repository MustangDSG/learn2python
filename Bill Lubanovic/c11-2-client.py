from datetime import datetime
import zmq

host = '127.0.0.1'
port = 5000

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))

request_str = "What time is it?"
request_bytes = request_str.encode('utf-8')
client.send(request_bytes)

reply_bytes = client.recv()
reply_str = reply_bytes.decode('utf-8')

print(reply_str)
 
