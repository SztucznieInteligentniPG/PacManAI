import numpy as np
import random
from tensorflow import keras
from tensorflow.keras import layers


def create():
    return keras.Sequential([
        keras.Input(shape=(19, 19, 10)),
        # layers.Conv2D(32, 3, activation='relu'),
        # layers.MaxPooling2D(2),
        # layers.Conv2D(32, 3, activation='relu'),
        # layers.MaxPooling2D(2),
        # layers.Conv2D(32, 3, activation='relu'),
        # layers.Flatten(),
        # layers.Dense(16, activation='relu'),
        # layers.Dense(4, activation='relu'),

        # layers.Conv2D(32, 3, activation='relu', padding='same', bias_initializer='random_uniform'),
        # layers.Conv2D(32, 3, activation='relu', padding='same', bias_initializer='random_uniform'),
        # layers.MaxPool2D(2),
        # layers.Conv2D(64, 3, activation='relu', bias_initializer='random_uniform'),
        # layers.Conv2D(64, 3, activation='relu', bias_initializer='random_uniform'),
        # layers.MaxPool2D(2),
        # layers.Flatten(),
        # layers.Dense(32, activation='relu', bias_initializer='random_uniform'),
        # layers.Dense(4, activation='softmax', bias_initializer='random_uniform')

        layers.Conv2D(32, 3, activation='tanh', padding='same', bias_initializer='random_uniform'),
        layers.Conv2D(32, 3, activation='tanh', padding='same', bias_initializer='random_uniform'),
        layers.MaxPool2D(2),
        layers.Conv2D(64, 3, activation='tanh', bias_initializer='random_uniform'),
        layers.Conv2D(64, 3, activation='tanh', bias_initializer='random_uniform'),
        layers.MaxPool2D(2),
        layers.Flatten(),
        layers.Dense(32, activation='tanh', bias_initializer='random_uniform'),
        layers.Dense(4, activation='sigmoid', bias_initializer='random_uniform')
    ])


def crossover(parent1: list, parent2: list) -> list:
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    # child = [
    #     np.zeros((3, 3, 10, 32)),
    #     np.zeros(32),
    #     np.zeros((3, 3, 32, 32)),
    #     np.zeros(32),
    #     np.zeros((3, 3, 32, 32)),
    #     np.zeros(32),
    #     np.zeros((32, 16)),
    #     np.zeros(16),
    #     np.zeros((16, 4)),
    #     np.zeros(4),
    # ]
    child = list(map(lambda x: np.zeros(x.shape), parent1))

    for layer in range(child.__len__()):
        dimensions = child[layer].shape.__len__()
        if dimensions == 4:
            crossConvolutionLayers(child, parent1, parent2, layer)
        elif dimensions == 2:
            crossDenseLayers(child, parent1, parent2, layer)
        elif dimensions == 1:
            crossBiasLayers(child, parent1, parent2, layer)

    # crossConvolutionLayers(child, parent1, parent2, 0)
    # crossConvolutionLayers(child, parent1, parent2, 2)
    # crossConvolutionLayers(child, parent1, parent2, 4)
    # crossDenseLayers(child, parent1, parent2, 6)
    # crossDenseLayers(child, parent1, parent2, 8)

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


def crossBiasLayers(child: list, parent1: list, parent2: list, layer: int):
    # shape - (bias (Count))
    crossoverPoint = random.randint(1, child[layer].shape[0])
    parents = [parent1, parent2]
    startParent = random.choice([0, 1])

    for i in range(child[layer].shape[0]):
        parent = startParent if i < crossoverPoint else 1 - startParent
        child[layer][i] = parents[parent][layer][i]



def crossoverCut(parent1: list, parent2: list) -> (list, list):
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    # child = [
    #     np.zeros((3, 3, 10, 32)),
    #     np.zeros(32),
    #     np.zeros((3, 3, 32, 32)),
    #     np.zeros(32),
    #     np.zeros((3, 3, 32, 32)),
    #     np.zeros(32),
    #     np.zeros((32, 16)),
    #     np.zeros(16),
    #     np.zeros((16, 4)),
    #     np.zeros(4),
    # ]
    child1 = list(map(lambda x: np.zeros(x.shape), parent1))
    child2 = list(map(lambda x: np.zeros(x.shape), parent1))
    serializedChild1 = []
    serializedChild2 = []
    serializedParent1 = serializeParent(parent1)
    serializedParent2 = serializeParent(parent2)

    crossoverPointsCount = crossoverPoint = random.randint(2,20 )
    crossoverPoints = []
    for i in range(crossoverPointsCount):
        crossoverPoints.append(random.randint(1, len(serializedParent1)))
    crossoverPoints.sort()
    currentParent = random.choice([-1, 1])
    for index, (el1, el2) in enumerate(zip(serializedParent1, serializedParent2)):
        if currentParent < 0:
            serializedChild1.append(el1)
            serializedChild2.append(el2)
        else:
            serializedChild1.append(el2)
            serializedChild2.append(el1)
        if index in crossoverPoints:
            currentParent *= -1

    child1 = deserializeChild(child1,serializedChild1)
    child2 = deserializeChild(child2,serializedChild2)
    # crossConvolutionLayers(child, parent1, parent2, 0)
    # crossConvolutionLayers(child, parent1, parent2, 2)
    # crossConvolutionLayers(child, parent1, parent2, 4)
    # crossDenseLayers(child, parent1, parent2, 6)
    # crossDenseLayers(child, parent1, parent2, 8)

    return child1, child2

def serializeParent(parent: list) -> list:
    serializedParent = []
    for layer in range(parent.__len__()):
        dimensions = parent[layer].shape.__len__()
        if dimensions == 4:
            serializedParent = serializeConvolutionLayers(serializedParent, parent, layer)
        elif dimensions == 2:
            serializedParent = serializeDenseLayers(serializedParent, parent, layer)
        elif dimensions == 1:
            serializedParent = serializeBiasLayers(serializedParent, parent, layer)
    return serializedParent

def deserializeChild(child:list, serialized:list):
    for layer in range(child.__len__()):
        dimensions = child[layer].shape.__len__()
        if dimensions == 4:
            child, serialized = deserializeConvolutionLayers(child, serialized, layer)
        elif dimensions == 2:
            child, serialized = deserializeDenseLayers(child, serialized, layer)
        elif dimensions == 1:
            child, serialized = deserializeBiasLayers(child, serialized, layer)
    return child

def serializeConvolutionLayers(serializedParent: list, parent: list, layer: int):
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    for pL in range(parent[layer].shape[2]):
        for nL in range(parent[layer].shape[3]):
            for x in range(parent[layer].shape[0]):
                for y in range(parent[layer].shape[1]):
                    serializedParent.append(parent[layer][x][y][pL][nL])

    return serializedParent

def deserializeConvolutionLayers(child: list,serialized: list, layer: int):
    # shape - (x, y, previousLayer (Count), nextLayer (Count))
    for pL in range(child[layer].shape[2]):
        for nL in range(child[layer].shape[3]):
            for x in range(child[layer].shape[0]):
                for y in range(child[layer].shape[1]):
                    child[layer][x][y][pL][nL] = serialized.pop(0)

    return child, serialized

def serializeDenseLayers(serializedParent: list, parent: list, layer: int):
    # shape - (previousLayer (Count), nextLayer (Count))
    for pL in range(parent[layer].shape[0]):
        for nL in range(parent[layer].shape[1]):
            serializedParent.append(parent[layer][pL][nL])
    return serializedParent

def deserializeDenseLayers(child: list, serialized: list, layer: int):
    # shape - (previousLayer (Count), nextLayer (Count))
    for pL in range(child[layer].shape[0]):
        for nL in range(child[layer].shape[1]):
            child[layer][pL][nL] = serialized.pop(0)
    return child, serialized


def serializeBiasLayers(serializedParent: list, parent: list, layer: int):
    # shape - (bias (Count))
    #crossoverPoint = random.randint(1, child[layer].shape[0])
    for i in range(parent[layer].shape[0]):
        serializedParent.append(parent[layer][i])
    return serializedParent

def deserializeBiasLayers(child: list, serialized: list, layer: int):
    # shape - (bias (Count))
    #crossoverPoint = random.randint(1, child[layer].shape[0])
    for i in range(child[layer].shape[0]):
        child[layer][i] = serialized.pop(0)
    return child, serialized



def mutate(weights: list, mutation_rate: float) -> list:
    for layer in range(weights.__len__()):
        dimensions = weights[layer].shape.__len__()
        if dimensions == 4:
            mutateConvolutionLayers(weights, mutation_rate, layer)
        elif dimensions == 2:
            mutateDenseLayers(weights, mutation_rate, layer)
        elif dimensions == 1:
            mutateBiasLayers(weights, mutation_rate, layer)

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


def mutateBiasLayers(weights: list, mutation_rate: float, layer: int):
    for i in range(weights[layer].shape[0]):
        if random.random() < mutation_rate:
            weights[layer][i] = random.uniform(-1, 1)


if __name__ == '__main__':
    model = create()
    model.summary()

    shapes = list(map(lambda x: x.shape, model.get_weights()))
    print(model.get_weights()[3])
