'''
Python Algorithm Untuk Data Logger Pembacaan Tegangan dan Arus Listrik
Develop by : Made Agus Andi Gunawan
IDN Maker Space Algoritm Factory

'''

# Import Library
import csv
import random
import time
import sys
import board
import math
import busio
import adafruit_ads1x15.ads1015 as ADS
from matplotlib.animation import FuncAnimation
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Pemanggilan ADC modul I2C
ads = ADS.ADS1015(i2c)

# Variabel masukan analog A0-A3
chan1 = AnalogIn(ads, ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)

# Definisi variabel
x_value = 0
tegangan1 = 0
nilai =0 
tegangan2 = 0
samples = 200

# pembuatan header file CSV
fieldname = ["x_value", "tegangan 1", "tegangan 2", "teganganrms", "nilai", "bacaan"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    csv_writer.writeheader()

# Perulangan pengambilan data sensor
while True:
    try:
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
            
            count = int(0)
            readVal = 0
            IrmsA = 0
            ampsA = 0
            maxValue = 0
            voltage = float(0)
            
            while count < samples:
                count +=1
                
                readVal= float(chan2.value)
                
                if readVal > maxValue:
                    maxValue = readVal
                
                    print("max value ", maxValue)
                    
                    info={
                        "x_value" : x_value,
                        "tegangan 1" : tegangan1,
                    }

                
                csv_writer.writerow(info)
                print(x_value, maxValue)
         
                x_value += 1
                tegangan1 = chan1.voltage
                tegangan2 = chan2.voltage
                nilai = chan2.value
                
    except KeyboardInterrupt:
            print('Program Dihentikan')
            sys.exit()
    
        


