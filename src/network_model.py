import numpy as np
import random
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


def crossover(parent1: list, parent2: list) -> list:
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    child = [
        np.zeros((3, 3, 10, 32)),
        np.zeros(32),
        np.zeros((3, 3, 32, 32)),
        np.zeros(32),
        np.zeros((3, 3, 32, 32)),
        np.zeros(32),
        np.zeros((32, 16)),
        np.zeros(16),
        np.zeros((16, 4)),
        np.zeros(4),
    ]

    crossConvolutionLayers(child, parent1, parent2, 0)
    crossConvolutionLayers(child, parent1, parent2, 2)
    crossConvolutionLayers(child, parent1, parent2, 4)
    crossDenseLayers(child, parent1, parent2, 6)
    crossDenseLayers(child, parent1, parent2, 8)

    return child


def crossConvolutionLayers(child: list, parent1: list, parent2: list, layer: int):
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    for pL in range(child[layer].shape[2]):
        for nL in range(child[layer].shape[3]):
            parent = random.choice([parent1, parent2])
            for x in range(child[layer].shape[0]):
                for y in range(child[layer].shape[1]):
                    child[layer][x][y][pL][nL] = parent[layer][x][y][pL][nL]


def crossDenseLayers(child: list, parent1: list, parent2: list, layer: int):
    # shape - (previousLayer (Count), nextLayer (Count))
    for pL in range(child[layer].shape[0]):
        for nL in range(child[layer].shape[1]):
            parent = random.choice([parent1, parent2])
            child[layer][pL][nL] = parent[layer][pL][nL]


def mutate(weights: list, mutation_rate: float) -> list:
    mutateConvolutionLayers(weights, mutation_rate, 0)
    mutateConvolutionLayers(weights, mutation_rate, 2)
    mutateConvolutionLayers(weights, mutation_rate, 4)
    mutateDenseLayers(weights, mutation_rate, 6)
    mutateDenseLayers(weights, mutation_rate, 8)

    return weights


def mutateConvolutionLayers(weights: list, mutation_rate: float, layer: int):
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    for pL in range(weights[layer].shape[2]):
        for nL in range(weights[layer].shape[3]):
            for x in range(weights[layer].shape[0]):
                for y in range(weights[layer].shape[1]):
                    if random.random() < mutation_rate:
                        weights[layer][x][y][pL][nL] = random.uniform(-1, 1)


def mutateDenseLayers(weights: list, mutation_rate: float, layer: int):
    # shape - (previousLayer (Count), nextLayer (Count))
    for pL in range(weights[layer].shape[0]):
        for nL in range(weights[layer].shape[1]):
            if random.random() < mutation_rate:
                weights[layer][pL][nL] = random.uniform(-1, 1)