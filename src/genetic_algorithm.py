from functools import reduce
import random

import network_model


def initialPopulation(size) -> list:
    population = []

    for i in range(size):
        population.append(network_model.create().get_weights())

    return population


def sortedProbabilities(scores: list) -> dict:
    minimum = min(scores)
    if minimum < 0:
        scores = list(map(lambda x: x - minimum + 1, scores))

    totalScore = reduce(lambda x, y: x + y, scores)
    probabilities = enumerate(map(lambda x: x / totalScore, scores))

    return {k: v for k, v in sorted(probabilities, key=lambda item: item[1], reverse=True)}


def selection(population: list, scores: list, elite: int) -> list:
    probabilities = sortedProbabilities(scores)

    selected = []

    for i, _ in list(probabilities.items())[:elite]:
        selected.append(population[i])

    for _ in range(population.__len__() - elite):
        rand = random.random()

        for i, p in probabilities.items():
            rand -= p

            if rand < 0:
                selected.append(population[i])
                break

    return selected


def crossover(population: list, elite: int) -> list:
    children = []

    for i in range(elite):
        children.append(population[i])

    for _ in range(population.__len__() - elite):
        parent1 = random.choice(population)
        parent2 = random.choice(population)

        child = network_model.crossover(parent1, parent2)
        children.append(child)

    return children


def mutation(population: list, mutationRate: float) -> list:
    for i in range(population.__len__()):
        population[i] = network_model.mutate(population[i], mutationRate)

    return population


def newGeneration(population: list, scores: list, elite: int, mutationRate: float) -> list:
    population = selection(population, scores, elite)
    population = crossover(population, elite)
    population = mutation(population, mutationRate)

    return population
