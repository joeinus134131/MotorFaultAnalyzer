import time
import sys
import math

from numpy import place
import Adafruit_ADS1x15
from ampread_python2 import IrmsA

adc = Adafruit_ADS1x15.ADS1015(address=0x48, busnum=1)

GAIN_A = 4
samples = 200
places = int(2)

while True:
    try:
        count = int(0)
        data = 0
        maxValue = 0
        IrmsA=0
        ampsA = 0
        voltage = float(0)
        kilowatts=float(0)

        #menghitung nila rms
        while count < samples:
            count +=1

            data = abs(adc.read_adc(1, gain=GAIN_A))

            if data > maxValue:
                maxValue = data

            #konversi tegangan ke arus 
            IrmsA = float(maxValue/float(2047)*30)
            IrmsA = round(IrmsA, places)
            ampsA = IrmsA/math.sqrt(2)

            ampsA = round(ampsA, places)