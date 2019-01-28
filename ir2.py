#Простейший файл-шаблон для обработки сигналов с ик-пульта.
import lirc

while True:
    sockid = lirc.init("myprogram")
    irkey = lirc.nextcode()
    if irkey[0]  == 'key1':
        print("Key 1 pressed!")
    elif irkey[0] == 'key2':
    	print("Key 2 pressed!")
    elif irkey[0] == 'key3':
    	print("Key 3 pressed!")
    elif irkey[0] == 'key4':
    	print("Key 4 pressed!")
    elif irkey[0] == 'key5':
    	print("Key 5 pressed!")
    elif irkey[0] == 'key6':
    	print("Key 6 pressed!")
    elif irkey[0] == 'key7':
    	print("Key 7 pressed!")
    elif irkey[0] == 'key8':
    	print("Key 8 pressed!")
    elif irkey[0] == 'key9':
    	print("Key 9 pressed!")
    elif irkey[0] == 'key0':
    	print("Key 0 pressed!")
    elif irkey[0] == 'keystar':
    	print("Key * pressed!")
    elif irkey[0] == 'keydiez':
    	print("Key # pressed!")
    elif irkey[0] == 'keyup':
    	print("Key up pressed!")
    elif irkey[0] == 'keydown':
    	print("Key down pressed!")
    elif irkey[0] == 'keyleft':
    	print("Key left pressed!")
    elif irkey[0] == 'keyright':
    	print("Key right pressed!")
    elif irkey[0] == 'keyok':
    	print("Key OK pressed!")
    else:
    	print("Howd u do that?!")
    lirc.deinit()
