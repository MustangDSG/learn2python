import smbus2
import bme280

# подрубаем датчик
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# считывание показаний
data = bme280.sample(bus, address, calibration_params)

# вывод
print ('''Показания BME280 на''',data.timestamp)
print ('''Температура =''', data.temperature)
print ('''Давление (мм рт ст) =''', data.pressure/1.33)
print ('''Давление (гПа) =''', data.pressure)
print ('''Относительная влажность =''', data.humidity)