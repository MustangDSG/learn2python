#BME280 v1.2
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
def createlist (ldata, param):
    ldata.append(param)
    return ldata

def updatelist (ldata, param):
    ldata.pop(0)
    ldata.append(param)
    return ldata

def midval (ldata, razm):
    summ = 0
    for i in ldata:
        summ = summ + i
    summ = summ/razm
    return summ
    
#Списки и переменные
ltemp = []
lpres = []
lhumi = []
lrazm = 10                  #размер списка
sleeptime = 5               #период обновления

#Основной цикл
while True:
    data = bme280.sample(bus, address, calibration_params)
    if len(ltemp) < lrazm:
        createlist(ltemp, data.temperature)
        createlist(lpres, data.pressure)
        createlist(lhumi, data.humidity)
    else:
        updatelist(ltemp, data.temperature)
        updatelist(lpres, data.pressure)
        updatelist(lhumi, data.humidity)
        print ('''Показания BME280 на''', data.timestamp)
        print ('''Температура =''', midval(ltemp, lrazm))
        print ('''Давление (гПа) =''', midval(lpres, lrazm))
        print ('''Относительная влажность =''', midval(lhumi, lrazm))
        time.sleep(sleeptime)
        os.system('clear')
# конец

