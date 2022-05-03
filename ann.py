import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense, Dropout
import keras.backend as K
from keras.losses import categorical_crossentropy

# Training data test
from sklearn.model_selection import train_test_split

# scaling data
from sklearn.preprocessing import StandardScaler

# Laporan Klasifikasi
from sklearn.metrics import classification_report
from keras.utils.np_utils import to_categorical
from sklearn.metrics import confusion_matrix

# membuat data frame
df = pd.read_csv('data.csv')

# menghilangkan missing value
na = pd.notnull(df["Position"])
df = df[na]

df = df[["Position", 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes']]

forward_player = ["ST", "LW", "RW", "LF", "RF", "RS","LS", "CF"]
midfielder_player = ["CM","RCM","LCM", "CDM","RDM","LDM", "CAM", "LAM", "RAM", "RM", "LM"]
defender_player = ["CB", "RCB", "LCB", "LWB", "RWB", "LB", "RB"]

df.loc[df["Position"] == "GK", "Position"] = 0

df.loc[df["Position"].isin(defender_player), "Position"] = 1

df.loc[df["Position"].isin(midfielder_player), "Position"] = 2

df.loc[df["Position"].isin(forward_player), "Position"] = 3

x = df.drop("Position", axis = 1)
sc = StandardScaler()
x = pd.DataFrame(sc.fit_transform(x))
y = df["Position"]

# membuat kolom prediksi kategori
y_cat = to_categorical(y)

# train test split
x_train, x_test, y_train, y_test = train_test_split(x.values, y_cat, test_size=0.2)

# membangun model
model = Sequential()
model.add(Dense(60, input_shape= (33,), activation= 'relu'))
model.add(Dense(15, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(4, activation='softmax'))

# kompilasi model
model.compile(optimizer='Adam', loss=categorical_crossentropy, metrics=['accuracy'])

# convert model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# simpan model
with open('model.tflite', 'wb') as f:
       f.write(tflite_model)

# ringkasan model
model.summary()

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), verbose=True, epochs=10)



# confusion matrics
y_pred_class = model.predict_classes(x_test)
from sklearn.metrics import confusion_matrix
y_pred = model.predict(x_test)
y_test_class = np.argmax(y_test, axis=1)
confusion_matrix(y_test_class, y_pred_class)


#print(classification_report(y_test_class, y_pred_class))

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