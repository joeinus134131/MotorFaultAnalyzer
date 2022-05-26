'''
Python Algorithm Untuk Data Logger Pembacaan Tegangan dan Arus Listrik
Develop by : Made Agus Andi Gunawan
IDN Maker Space Algoritm Factory
'''

# Import Library
import random
import time
import sys
import board
import math
import busio
from time import sleep
from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import adafruit_ads1x15.ads1015 as ADS
from matplotlib.animation import FuncAnimation
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Pemanggilan ADC modul I2C
ads = ADS.ADS1015(i2c)

# Variabel masukan analog A0-A3

# Definisi variabel
x_value = 0
tegangan1 = 0
nilai =0 
tegangan2 = 0
samples = 200

# Perulangan pengambilan data sensor
while True:
    try:      
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
            
            count = int(0)
            datasensing = [0]*4
            dataanalog = [0]*4
            maxValue = [0]*4
            Irms = 0
            amps = 0
            tegangan = [0]*4
            #voltage = float(0)
            
            while count < samples:
                count +=1
                for i in range(0,2):
                    datasensing[i]= float(chan[i].voltage)
                
                    if datasensing[i] > tegangan[i]:
                        tegangan[i] = datasensing[i]
                
                dataanalog[i] = float(chan[i].value)
                if dataanalog[i] > maxValue[i]:
                    maxValue[i] = dataanalog[i]

                arus = float(maxValue[3])
                Irms = float(arus / float(2047) * 30)
                Irms = round(Irms, adbk)
                amps = Irms / math.sqrt(2)
                amps = round(amps, adbk)

                info = {
                    "x_value": x_value,
                    "Tegangan 1": tegangan[0],
                    "Tegangan 2": tegangan[1],
                    "Tegangan 3": tegangan[2],
                    "Value": maxValue[0],
                    "Arus": amps,
                }
                
            csv_writer.writerow(info)
            print(x_value, tegangan[0], tegangan[1], tegangan[2], maxValue[0], amps)
         
            x_value += 1
            tegangan1 = tegangan[0]
            tegangan2 = tegangan[1]
            tegangan3 = tegangan[2]
            maxValue = maxValue[0]
            amps = amps
                
    except KeyboardInterrupt:
            print('Program Dihentikan')
            sys.exit()