#Циклический сбор данных с датчика BME280 и вывод показаний на lcd дисплей 1602.
#Блок импорта
import smbus2, bme280, lcddriver
import os, time

#Подключаем дисплей.
display = lcddriver.lcd()
display_strings = ['None', 'None']

#Подключаем датчик
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

#Время обновления показаний в секундах.
upd_time = 5

#Основной цикл
while True:
	data = bme280.sample(bus, address, calibration_params)
	temp = str(round(data.temperature, 2))
	pres = str(round(data.pressure, 2))
	humi = str(round(data.humidity, 2))
	pre2 = str(round(data.pressure/1.33322, 2))
	
	display.lcd_clear()
	display.lcd_display_string(temp+"C"+" "+pres, 1)
	display.lcd_display_string(humi+"%"+" "+pre2, 2)
	
	time.sleep(upd_time)


