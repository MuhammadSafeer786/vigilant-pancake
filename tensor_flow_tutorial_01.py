# -*- coding: utf-8 -*-
"""tensor_flow_tutorial_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W5p9lnT3h0gO8apYgOO9rbtuzpW-U1L4
"""

import tensorflow as tf

import numpy as np

celsius_q = np.array([-40,-10,0,8,15,22,38], dtype=float)
fahrenheit_a = np.array([-40,14,32,46,59,72,100], dtype=float)

for i,c in enumerate(celsius_q):
  print("{} degrees Celsius = {} degrees Fahrenheit".format(c,fahrenheit_a[i]))

layer_0 = tf.keras.layers.Dense(units=1,input_shape=[1])

model = tf.keras.Sequential([layer_0])

model.compile(loss="mean_squared_error",
              optimizer=tf.keras.optimizers.Adam(0.1)) # where 0.1 is learning rate

my_model = model.fit(celsius_q,fahrenheit_a,epochs=500,verbose=False)

import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel('Loss Magnitude')
plt.plot(my_model.history['loss'])

print(model.predict([100.0]))

"""Looking at layer weights"""

print("These are layer variables: {}".format(layer_0.get_weights()))

"""If i add more layers, the variables 1.8 and 28 (which is 32 in real equation) changes, but the answer remains the same."""

layer_0 = tf.keras.layers.Dense(units=4,input_shape=[1])
layer_1 = tf.keras.layers.Dense(units=4)
layer_2 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([layer_0,layer_1,layer_2])
model.compile(loss="mean_squared_error",
              optimizer=tf.keras.optimizers.Adam(0.1))
my_model = model.fit(celsius_q,fahrenheit_a,epochs=500,verbose=False)

"""Now if i print the weights, they are not even close to the real constants in the equation of finding 'degree F' from 'degree c'.  but the answer is still prity much the same."""

print(model.predict([100.0]))

print('The weights are :{} \n And :{}\n And :{}', layer_0.get_weights(),layer_1.get_weights(),layer_2.get_weights(),)