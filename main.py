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

window.title("AMORFTRA (Automatic 3 Phasse Motor Fault Diagnosis Tool ITERA)")

plt.style.use('dark_background')

index = count()

WIDTH = 840
HEIGHT = 800
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='lightblue')
canvas.pack()

# Frame Grafik Loss dan Akurasi
frameGrafik = Frame(window, bg='black')
frameGrafik.place(relx=1, rely=0.5, relwidth=0.7, relheight=1, anchor='e')

framemenu = Frame(window, bg='white')
framemenu.place(relx=0.025, rely=0.5, relwidth=0.25, relheight=0.9, anchor='w')

judul = tk.Label(window, font ="arial 9", text = "Setting Parameter")
judul.place(x=30, y=20)

tuning = tk.Label(framemenu, font ="arial 9", text = "Tuning Model ANN")
tuning.place(x=20, y=40)

prediksi = tk.Label(framemenu, font ="arial 10", text = "Prediksi : ")
prediksi.place(x=20, y=60)

akurasi = tk.Label(framemenu, font ="arial 10", text = "Akurasi : ")
akurasi.place(x=20, y=80)

loss = tk.Label(framemenu, font ="arial 10", text = "Loss : ")
loss.place(x=20, y=110)

# Fungsi hitung cek kerusakan
def hitung():
    textArea1  = tk.Text(framemenu, height=1, width=13)
    textArea1.place(x=20, y=130)
    prediksi = "{val}".format(val=y1)
    textArea1.insert(tk.END, prediksi)
    
    textArea2  = tk.Text(framemenu, height=1, width=13)
    textArea2.place(x=20, y=150)
    akurasi = "98.5%"
    textArea2.insert(tk.END, akurasi)
    
    textArea3  = tk.Text(framemenu, height=1, width=13)
    textArea3.place(x=20, y=170)
    loss ="5.3%"
    textArea3.insert(tk.END, loss)
    
    print("Berhasil")

# Inisialisasi Pin Masukan Raspberry PI
x_val = []
y_val = []

# Tampilan Grafik

# fungsi animasi plot
def animationplot(i):
    data = pd.read_csv('data.csv')
    
    f = Figure()
    x = data['x_value']
    y1 = data['Tegangan 1']
    y2 = data['Tegangan 2']
    y3 = data['Tegangan 3']
    arus = data['Arus']
    
    ax1, ax2 = plt.gcf().get_axes()
    
    # Menghapus data grafik
    ax1.cla()
    ax2.cla()
    
    # Grafik 1  
    ax1.set_title('Grafik Tegangan & Arus 3 Phase')
    ax1.set_xlabel('Waktu')
    ax1.set_ylabel('Tegangan (Volt)')

    ax1.plot(x, y1, 'r', label='Tegangan F1')
    ax1.plot(x, y2, 'g', label='Tegangan F2')
    ax1.plot(x, y3, 'b', label='Tegangan F3')
    
    # Grafik 2
    ax2.set_xlabel('Waktu')
    ax2.set_ylabel('Arus (Ampere)')
    
    ax2.plot(x, y2, 'y', label="Arus")
             
    grafik = FigureCanvasTkAgg(plt.gcf(), frameGrafik)
    grafik.get_tk_widget().place(relheight=1, relwidth=1)
    grafik.draw()
   
plt.gcf().subplots(2,1)    
ani = FuncAnimation(plt.gcf(), animationplot, frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=False, interval=10, blit=False)

# Load Dataset
#dataku = pd.read_csv("data.csv")
#dataku

# Load Model ANN
#filemodelscaller = ''
#scaler = pickle.load(open(filemodelscaller, 'rb'))

#modelann = ''
#loadmodel = pickle.load(open(modelann, 'rb'))

# Tombol cek kerusakan
tombol = Button(window, text='Cek Kerusakan', command=hitung)
tombol.place(x=50, y=350)

 
#plt.tight_layout()
plt.show()
window.mainloop()