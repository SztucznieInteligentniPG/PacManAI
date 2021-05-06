from tensorflow import keras
from tensorflow.keras import layers


def create():
    return keras.Sequential([
        keras.Input(shape=(19, 19, 10)),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(2),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(2),
        layers.Conv2D(32, 3, activation='relu'),
        layers.Flatten(),
        layers.Dense(16, activation='relu'),
        layers.Dense(4, activation='relu'),
    ])
