#BME280 v1.1
#Циклический сбор данных с датчика BME280 в списки и вывод среднего значения.
#Блок импорта
import smbus2
import bme280
import os
import time


#Самое начало
os.system('clear')

#Подрубаем датчик
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

#Считывание показаний (перенесено в основной цикл, иначе не будем получать новые значения)
#data = bme280.sample(bus, address, calibration_params)

#Блок функций
def midval (ldata, razm):
    summ = 0
    for i in ldata:
        summ = summ + i
    summ = summ/razm
    return summ

#Списки (пока мясом)
ltemp = []
lpres = []
lhumi = []
lrazm = 10                  #размер списка
sleeptime = 5               #период обновления

#Основной цикл (пока мясом)
while True:
    data = bme280.sample(bus, address, calibration_params)
    if len(ltemp) < lrazm:
        ltemp.append(data.temperature)
        lpres.append(data.pressure)
        lhumi.append(data.humidity)
    else:
        ltemp.pop(0)
        lpres.pop(0)
        lhumi.pop(0)
        ltemp.append(data.temperature)
        lpres.append(data.pressure)
        lhumi.append(data.humidity)
        print ('''Показания BME280 на''', data.timestamp)
        print ('''Температура =''', midval(ltemp, lrazm))
        print ('''Давление (гПа) =''', midval(lpres, lrazm))
        print ('''Относительная влажность =''', midval(lhumi, lrazm))
        time.sleep(sleeptime)
        os.system('clear')
# конец

