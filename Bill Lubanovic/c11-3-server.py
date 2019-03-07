from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer

def responz(wtisit):
	if wtisit == "What time is it?":
		return datetime.now().isoformat()

server = SimpleXMLRPCServer(("localhost", 5000))
server.register_function(responz)
server.serve_forever()
