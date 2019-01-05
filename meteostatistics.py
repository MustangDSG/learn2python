#Метеостатистика v.1.0
#Сбор данных с датчика и запись в базу данных.


#блок импорта
import smbus2, bme280
import sqlite3
import os, time

#подрубаем датчик
port=1
address=0x76
bus=smbus2.SMBus(port)
calibration_params=bme280.load_calibration_params(bus, address)

#подруб базы
BASE_DIR=os.path.dirname(os.path.abspath(__file__))		#этот код заставляет искать файл базы в папке,
db_path=os.path.join(BASE_DIR, "meteos.sqlite3")		#откуда запускается данный скрипт
dbconnect=sqlite3.connect(db_path)
cursor=dbconnect.cursor()

#создание таблицы
cursor.execute("""CREATE TABLE meteodata (
	timestamp TEXT PRIMARY KEY,
	temperature INTEGER,
	pressure INTEGER,
	humidity INTEGER
	) """)

sleeptime=300            								#период обновления (в секундах)

#основной цикл
while True:
	data=bme280.sample(bus, address, calibration_params)
	timestamp=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
	meteostats=[(timestamp, data.temperature, data.pressure, data.humidity)]
	cursor.executemany("INSERT INTO meteodata VALUES (?,?,?,?)", meteostats)
	time.sleep(sleeptime)
#конец