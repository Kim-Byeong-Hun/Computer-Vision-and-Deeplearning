# 다층 퍼셉트론으로 MNIST 인식하기(SGD와 Adam의 성능 그래프 비교)
# 다층 퍼셉트론으로 MNIST 인식하기(SGD Optimizer)
import numpy as np
import tensorflow as tf
import keras.datasets as ds

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD, Adam

import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = ds.mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# SGD optimizer 사용
mlp_sgd = Sequential()
mlp_sgd.add(Dense(units=512, activation='tanh', input_shape=(784,)))
mlp_sgd.add(Dense(units=10, activation='softmax'))

mlp_sgd.compile(loss='MSE', optimizer=SGD(learning_rate=0.01), metrics=['accuracy'])
hist_sgd = mlp_sgd.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)

res_sgd = mlp_sgd.evaluate(x_test, y_test, verbose=0)
print('SGD 정확률=', res_sgd[1]*100)

# Adam Optimizer 사용
mlp_Adam = Sequential()
mlp_Adam.add(Dense(units=512, activation='tanh', input_shape=(784,)))
mlp_Adam.add(Dense(units=10, activation='softmax'))

mlp_Adam.compile(loss='MSE', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
hist_Adam = mlp_Adam.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)

res_Adam = mlp_Adam.evaluate(x_test, y_test, verbose=0)
print('Adam 정확률=', res_Adam[1]*100)

plt.plot(hist_sgd.history['accuracy'], 'r--')
plt.plot(hist_sgd.history['val_accuracy'], 'r')
plt.plot(hist_Adam.history['accuracy'], 'b--')
plt.plot(hist_Adam.history['val_accuracy'], 'b')
plt.title('Comparison of SGD and Adam optimizers')
plt.ylim((0.7, 1.0))
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(['train_sgd', 'val_sgd', 'train_adam', 'val_adam'])
plt.grid()
plt.show()