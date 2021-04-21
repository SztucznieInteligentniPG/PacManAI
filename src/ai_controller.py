import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from controller import Controller
from direction import Direction
from world import World


class AiController(Controller):
    direction: Direction = None

    def __init__(self, weights):
        self.model = keras.Sequential([
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
        if weights is not None:
            self.model.set_weights(weights)

    def update(self, world: World):
        data = tf.random.uniform(shape=(1, 19, 19, 10), maxval=1.0)

        max_arg = tf.math.argmax(self.model(data)[0])
        direction_index = max_arg.numpy()

        self.direction = Direction(direction_index)
