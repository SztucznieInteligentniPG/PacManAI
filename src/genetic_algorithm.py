import network_model


def initialPopulation(size) -> list:
    population = []

    for i in range(size):
        population.append(network_model.create().get_weights())

    return population


def selection(population, scores) -> list:
    return population


def crossover(population, scores) -> list:
    return population


def mutation(population, scores) -> list:
    return population


def newGeneration(population, scores) -> list:
    population = selection(population, scores)
    population = crossover(population, scores)
    population = mutation(population, scores)

    return population
