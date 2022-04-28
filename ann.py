import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import RMSprop
from keras.models import load_model
import tensorflow as tf
from ann_visualizer.visualize import ann_viz


dataset = pd.read_csv("/home/pi/Documents/TA2022/datalog.csv")
X = dataset.iloc[:, 0:8]
y = dataset.iloc[:, 8]

# Melihat dataset
print(dataset.head())

# Standarisasi Datasets
sc = StandardScaler()

# Transformasi data tabular ke array dengan StandardScaller transform
X = sc.fit_transform(X)

# Setting Optimizers
RMSprop(
    learning_rate=0.001,
    rho=0.9,
    momentum=0.0,
    epsilon=1e-07,
    centered=False,
    name="RMSprop"
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=32)

# Arsitektur Model ANN
model = Sequential()
model.add(Dense(12, input_dim=8, activation='tanh'))
model.add(Dropout(0.2))
model.add(Dense(8, activation='tanh'))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))

# Visualisasi Model
# ann_viz(model, view=True, filename='TA_ann.gv', title='Visualisasi ANN TA')

# Compile Model ANN
model.compile(optimizer= 'RMSprop', loss='MSE', metrics=['accuracy'])

# Training Model ANN
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=32)

# prediksi model
prediksi = model.predict(X_test)

# Evaluasi Model
score = model.evaluate(X_test, y_test, batch_size=32)
print("Score model :", score)

# Save Model
model.save('modelann.h5')

# Load Model
modelku = load_model('modelann.h5')

# list histori
print(history.history.keys())

# grafik akurasi
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Akurasi Model')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# grafik loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
