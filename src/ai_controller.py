import tensorflow as tf

from controller import Controller
from direction import Direction
import network_model
from world import World


class AiController(Controller):
    direction: Direction = None

    def __init__(self, weights):
        self.model = network_model.create()

        if weights is not None:
            self.model.set_weights(weights)

    def update(self, world: World):
        max_arg = tf.math.argmax(self.model(world.generateTensor())[0])
        direction_index = max_arg.numpy()

        self.direction = Direction(direction_index)
