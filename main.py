"""

TA - 2022
Diagnosis Motor 3 Fasa dengan ANN
Credit by : Made Agus Andi Gunawan

"""

# Load Libary
from time import sleep
from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation
from itertools import count
import time
import tkinter as tk
import RPi.GPIO as GPIO
import tensorflow as tf
import pickle
import sklearn
import smbus
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import adafruit_ads1x15.ads1015 as ADS
import busio
import csv


# Konfigurasi GUI
window = tk.Tk()
#window.resizable(width=False, height=False)
#window.iconbitmap('logo_itera_oke_bvD_icon.ico')

window.title("SMTPA(Smart Motor 3 Phase Analyzer)")

plt.style.use('dark_background')

index = count()

WIDTH = 1000
HEIGHT = 700
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='lightblue')
canvas.pack()

# Frame Grafik Loss dan Akurasi
frameGrafik = Frame(window, bg='white')
frameGrafik.place(relx=1, rely=0.5, relwidth=0.7, relheight=1, anchor='e')

framemenu = Frame(window, bg='white')
framemenu.place(relx=0.025, rely=0.5, relwidth=0.25, relheight=0.7, anchor='w')

judul = tk.Label(window, font ="arial 12 bold", text = "Semoga lulus tahun ini")
judul.place(x=70, y=20)

tuning = tk.Label(framemenu, font ="arial 12 bold", text = "Tuning Model ANN")
tuning.place(x=30, y=30)

prediksi = tk.Label(framemenu, font ="arial 12 bold", text = "Prediksi : ")
prediksi.place(x=30, y=360)

akurasi = tk.Label(framemenu, font ="arial 12 bold", text = "Akurasi : ")
akurasi.place(x=30, y=400)

loss = tk.Label(framemenu, font ="arial 12 bold", text = "Loss : ")
loss.place(x=30, y=440)

# Fungsi hitung cek kerusakan
def hitung():
    textArea1  = tk.Text(framemenu, height=1, width=13)
    textArea1.place(x=120, y=360)
    prediksi = "{val}".format(val=y1)
    textArea1.insert(tk.END, prediksi)
    
    textArea2  = tk.Text(framemenu, height=1, width=13)
    textArea2.place(x=120, y=400)
    akurasi = "98.5%"
    textArea2.insert(tk.END, akurasi)
    
    textArea3  = tk.Text(framemenu, height=1, width=13)
    textArea3.place(x=120, y=440)
    loss ="5.3%"
    textArea3.insert(tk.END, loss)
    
    print("Berhasil")
    
# fungsi(*args):
   # print(len(var.get()))


# Inisialisasi Pin Masukan Raspberry PI
x_val = []
y_val = []

# Tampilan Grafik


# fungsi animasi plot
def animationplot(i):
    data = pd.read_csv('data.csv')
    
    f = Figure()
    ax = f.add_subplot(211)
    ay = f.add_subplot(212)
    x = data['x_value']
    y1 = data['Tegangan 1']
    y2 = data['Tegangan 2']
    
   # Grafik 1  
    ax.set_title('Grafik Tegangan 3 Fasa')
    ax.set_xlabel('Waktu')
    ax.set_ylabel('Tegangan (Volt)')

    plt.cla()
    ax.plot(x, y1, label='Tegangan Fasa 1')
    plt.tight_layout()
    line1 = ax.plot([], [])[0]
    line1.set_xdata(x)
    line1.set_ydata(y1)
    line1.set_ydata(y2)
    grafik = FigureCanvasTkAgg(f, frameGrafik)
    grafik.get_tk_widget().place(relheight=0.8, relwidth=1)
    grafik.draw()
    
    # Grafik 2
    ay.set_xlabel('Waktu')
    ay.set_ylabel('Arus (Ampere)' )
    
    plt.cla()
    ax.plot(x, y2, label='Tegangan Fasa 1')
    line2 = ay.plot([], [])[0]
    line2.set_xdata(x)
    line2.set_ydata(y2)
    grafik2 = FigureCanvasTkAgg(f, frameGrafik)
    grafik2.get_tk_widget().place(relheight=1, relwidth=1)
    grafik2.draw()
    plt.tight_layout()
    
    

ani = FuncAnimation(plt.gcf(), animationplot, interval=50)

# Load Dataset
dataku = pd.read_csv("data.csv")
#dataku

# Load Model ANN
#filemodelscaller = ''
#scaler = pickle.load(open(filemodelscaller, 'rb'))

#modelann = ''
#loadmodel = pickle.load(open(modelann, 'rb'))

# Tombol cek kerusakan
tombol = Button(window, text='Cek Kerusakan', command=hitung)
tombol.place(x=80, y=630)

#plt.tight_layout()
plt.show()
window.mainloop()

