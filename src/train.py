from datetime import datetime
import multiprocessing
import os
import time


import genetic_algorithm as genetic
import network_model


def runTraining():
    import app

    populationSize = 100
    generations = 1000
    elite = 10
    mutationRate = 1 / 220000

    cpus = multiprocessing.cpu_count()
    print("Processors detected: ", cpus)

    trainingStart = datetime.now().strftime("%Y-%m-%d_%H;%M;%S")

    print('Generating population...')
    start = time.time()
    population = genetic.initialPopulation(populationSize)
    print('Generating complete:', time.time() - start, 's')

    maxScore = 0
    savingModel = network_model.create()

    for generation in range(generations):
        print('Generation', generation + 1, 'start')

        start = time.time()

        with multiprocessing.Pool(cpus) as pool:
            scores = pool.map(app.trainPlayer, population)

        print(
            'Generation', generation + 1, 'over;',
            'Simulation time:', time.time() - start, 's;',
            'Scores (', scores.__len__(), '):\n',
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

        population = genetic.newGeneration(population, scores, elite, mutationRate)


if __name__ == '__main__':
    # Wyłączenie wkurzających wiadomości
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    runTraining()
