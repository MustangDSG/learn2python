import lcddriver
import lirc

display = lcddriver.lcd()
display_strings = ['None', 'None']

def keypressed(keyp):
    display.lcd_clear()
    display_strings.pop(0)
    display_strings.append("Key "+keyp)


try:
    print("Writing to display")
    while True:
        display.lcd_display_string(display_strings[0], 1)
        display.lcd_display_string(display_strings[1], 2)

        sockid = lirc.init("myprogram")
        irkey = lirc.nextcode()

        if irkey[0]  == 'key1':
            keypressed('1')
        elif irkey[0] == 'key2':
            keypressed('2')

        elif irkey[0] == 'key3':
            keypressed('3')

        elif irkey[0] == 'key4':
            keypressed('4')

        elif irkey[0] == 'key5':
            keypressed('5')

        elif irkey[0] == 'key6':
            keypressed('6')

        elif irkey[0] == 'key7':
            keypressed('7')

        elif irkey[0] == 'key8':
            keypressed('8')

        elif irkey[0] == 'key9':
            keypressed('9')

        elif irkey[0] == 'key0':
            keypressed('0')

        elif irkey[0] == 'keystar':
            keypressed('*')

        elif irkey[0] == 'keydiez':
            keypressed('#')

        elif irkey[0] == 'keyup':
            keypressed('UP')

        elif irkey[0] == 'keydown':
            keypressed('DOWN')

        elif irkey[0] == 'keyleft':
            keypressed('LEFT')

        elif irkey[0] == 'keyright':
            keypressed('RIGHT')

        elif irkey[0] == 'keyok':
            keypressed('OK')

        else:
            keypressed("Howd u do that?!")
        lirc.deinit()

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
