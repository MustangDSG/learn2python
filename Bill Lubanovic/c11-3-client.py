from datetime import datetime
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")
text = "What time is it?"
print(proxy.responz(text))