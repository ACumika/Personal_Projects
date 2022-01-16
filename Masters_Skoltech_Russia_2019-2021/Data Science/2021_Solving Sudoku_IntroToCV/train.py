import joblib
import random

import torch
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# pip install python-mnist
from mnist import MNIST
# download 4 MNIST files you can here:
# http://yann.lecun.com/exdb/mnist/


MNIST_CELL_SIZE = 28
SEED = 0xBadCafe


#def fix_seed(seed=SEED):
#    random.seed(seed)
#    np.random.seed(seed)
#    torch.manual_seed(seed)
#    torch.backends.cudnn.deterministic = True
#    torch.backends.cudnn.benchmark = False


def train(save_model_path='cnn.joblib', mnist_data_path='mnist_data', print_accuracy=False):
    
    save_model_path = "."
    MNIST_CELL_SIZE = 28
    
    mnist_data_path = '.'
    mnist_data = MNIST(mnist_data_path)
    mnist_data.gz = True
    
    X_train, y_train = mnist_data.load_training()
    X_test, y_test = mnist_data.load_testing()
    
    
    X_train = np.uint8([np.reshape(im, (MNIST_CELL_SIZE,) * 2) for im in X_train])
    X_test = np.uint8([np.reshape(im, (MNIST_CELL_SIZE,) * 2) for im in X_test])
    y_train, y_test = np.int16(y_train), np.int16(y_test)
    
    X_train = X_train.reshape(60000, 28, 28, 1)
    X_test = X_test.reshape(10000, 28, 28, 1)
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    
    
    ## Declare the model
    model = Sequential()
    
    ## Declare the layers
    layer_1 = Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28, 1))
    layer_2 = Conv2D(64, kernel_size=3, activation='relu', dilation_rate=3)
    layer_3 = Flatten()
    layer_4 = Dense(10, activation='softmax')
    
    ## Add the layers to the model
    model.add(layer_1)
    model.add(layer_2)
    model.add(layer_3)
    model.add(layer_4)
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5)


    model.save('C:/Users/admin/Desktop/Skoltech/Intro to CV/HW2/mod3.h5')


        