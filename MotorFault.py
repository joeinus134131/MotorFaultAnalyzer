#program pembacaan arus listrik 3 fasa
import time
import sys
import math
import re
import datetime
import Adafruit_ADS1x15
from references import LINEV

# 
adc = Adafruit_ADS1x15.ADS1015(address=0x48, busnum=1)

GAIN_A = 4
samples = 200
places = int(2)
time_elapsed = (0)

while True:
    try:
        #Variabel
        count = int(0)
        data = [0] * 4
        maxValue = [0] * 4
        IrmsA = [0] * 4
        ampsA = [0] * 4
        voltage = float(0)
        kilowatts=float(0)

        start_time = time.time()

        #menghitung nila rms
        while count < samples:
            count +=1

            for i in range(0, 4):
                data[i] = abs(adc.read_adc(i, gain=GAIN_A))

                if data[i] > maxValue[i]:
                    maxValue[i] = data[i]

            for i in range(0,4):
                #konversi tegangan ke arus 
                IrmsA[i] = float(maxValue[i]/float(2047)*30)
                IrmsA[i] = round(IrmsA[i], places)
                ampsA[i] = IrmsA[i]/math.sqrt(2)

                ampsA[i] = round(ampsA[i], places)

        ampsA0 = ampsA[0]
        ampsA1 = ampsA[1]
        ampsA2 = ampsA[2]
        ampsA3 = ampsA[3]

        print("data 1 : ", ampsA0)
        print("data 2 : ", ampsA1)
        print("data 3 : ", ampsA2)
        print("data 4 : ", ampsA3)
        
        kilowatts = round((ampsA0+ampsA1+ampsA2+ampsA3)*LINEV/1000, places)

        kwh = round((kilowatts*time_elapsed)/3600, 8)

        print("kwh : ", kwh)

    except KeyboardInterrupt:
        print('Kamu Kembali dari program')
        sys.exit()