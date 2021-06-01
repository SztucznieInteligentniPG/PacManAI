from datetime import datetime
from itertools import repeat
import multiprocessing
import os
import random
import time


import genetic_algorithm as genetic
import network_model
from tracker import Tracker


def runTraining():
    import app

    populationSize = 100
    generations = 1000
    elite = 10
    mutationRate = 1 / 110000
    cpus = multiprocessing.cpu_count()
    print("Processors detected: ", cpus)

    trainingStart = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    tracker = Tracker('./statistics/' + trainingStart)

    print('Generating population...')
    start = time.time()
    population = genetic.initialPopulation(populationSize)
    print('Generating complete:', time.time() - start, 's')

    maxScore = 0
    savingModel = network_model.create()

    for generation in range(generations):
        print('Generation', generation + 1, 'start')
        start = time.time()

        seed = random.randint(0, 9223372036854775807)
        with multiprocessing.Pool(cpus) as pool:
            # scores = pool.map(app.trainPlayer, population)
            result = pool.starmap(app.trainPlayer, zip(population, repeat(seed)))
        scores = [item.data['pointsTotal'] for item in result]
        statistics = result
        tracker.setGeneration(statistics, generation)
        print(
            'Generation', generation + 1, 'over;',
            'Population count:', scores.__len__(), ';',
            'Simulation time:', time.time() - start, 's;',
            'Enemy seed:', seed, ';',
            'Scores:\n',
            scores,
        )

        maxIndex = 0
        for i in range(scores.__len__()):
            if scores[i] > scores[maxIndex]:
                maxIndex = i

        savingModel.set_weights(population[maxIndex])
        savingModel.save_weights('./training/' + trainingStart + '/best_gen_' + str(generation + 1))

        if scores[maxIndex] > maxScore:
            savingModel.save_weights('./training/' + trainingStart + '/best')
            maxScore = scores[maxIndex]

        for i in range(population.__len__()):
            savingModel.set_weights(population[i])
            savingModel.save_weights('./training/' + trainingStart + '/specimen_' + str(i))

        population = genetic.newGeneration(population, scores, elite, mutationRate)

        tracker.saveData()


if __name__ == '__main__':
    # Wyłączenie wkurzających wiadomości
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    runTraining()
