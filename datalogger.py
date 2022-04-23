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
        count = int(0)
        readVal = [0]*4
        IrmsA = [0]*4
        ampsA = [0] * 4
        maxValue = [0] * 4
        voltage = float(0)
            
        while count < samples:
            count +=1
                
            for i in range(0,4):
                chan[i] = AnalogIn(ads, ADS.P[i])
                
                readVal= float(chan[i].voltage)
                
                if readVal[i] > maxValue[i]:
                    maxValue[i] = readVal[i]
                
                    #print("max value ", maxValue[i])

        sensor1 = maxValue[0]  
        sensor2 = maxValue[1]
        sensor3 = maxValue[2]
        sensor4 = maxValue[3]
                
    except KeyboardInterrupt:
            print('Program Dihentikan')
            sys.exit()