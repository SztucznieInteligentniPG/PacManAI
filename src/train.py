import multiprocessing
import os
import time

import genetic_algorithm as genetic


def runTraining():
    import app

    populationSize = 100
    generations = 10

    cpus = multiprocessing.cpu_count()
    print("Processors detected: ", cpus)

    print('Generating population...')
    start = time.time()
    population = genetic.initialPopulation(populationSize)
    print('Generating complete:', time.time() - start, 's')

    for generation in range(generations):
        print('Generation', generation + 1, 'start')

        start = time.time()

        with multiprocessing.Pool(cpus) as pool:
            scores = pool.map(app.trainPlayer, population)

        print('Generation', generation + 1, 'over; Simulation time:', time.time() - start, 's; Scores:')
        print(scores)

        population = genetic.newGeneration(population, scores)


if __name__ == '__main__':
    # Wyłączenie wkurzających wiadomości
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    runTraining()
