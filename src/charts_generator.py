from matplotlib import pyplot as plt
import numpy as np
import string

from tracker import Tracker
class ChartsGenerator:
    tracker: Tracker

    def __init__(self, file: string):
        self.tracker = Tracker(file)
        self.tracker.load()

    def createPieChart(self):
        points = 0
        powerUps = 0
        ghosts = 0
        time = 0
        for gen in self.tracker.data:
            for ind in gen:
                points += ind['pointsPoints']
                powerUps += ind['pointsPowerUps']
                ghosts += ind['pointsGhosts']
                time += ind['pointsTime']

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        labels = ['Points', 'PowerUps', 'Time', 'Ghosts']
        students = [points, powerUps, time, ghosts]
        ax.pie(students, labels=labels, autopct='%1.2f%%')
        plt.show()

    def createDeathChart(self):
        deathCount=[]
        for gen in self.tracker.data:
            sum=0
            for ind in gen:
                sum += ind['deaths']
            deathCount.append(sum)

        plt.plot(range(len(deathCount)),deathCount,'ro')
        plt.show()

    def createStackedChart(self):

        pointsData = []
        powerUpsData = []
        ghostsData = []
        timeData = []
        for gen in self.tracker.data:
            points = 0
            powerUps = 0
            ghosts = 0
            time = 0
            for ind in gen["population"]:
                points += ind['pointsPoints']
                powerUps += ind['pointsPowerUps']
                ghosts += ind['pointsGhosts']
                time += ind['pointsTime']
            pointsData.append(points/500)
            powerUpsData.append(powerUps/500)
            ghostsData.append(ghosts/500)
            timeData.append(time/500)
        width = 1
        fig, ax = plt.subplots()
        ax.bar(range(len(pointsData)), pointsData, width, label='Points')
        ax.bar(range(len(powerUpsData)), powerUpsData, width, label='PowerUps')
        ax.bar(range(len(ghostsData)), ghostsData, width, label='Ghosts')
        ax.bar(range(len(timeData)), timeData, width, label='Time')

        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.legend()

        plt.show()

    def createHatChart(self):

        minPoints = []
        maxPoints = []
        avgPoints = []
        for gen in self.tracker.data:
            points = 0
            min = gen[0]['pointsTotal']
            max = gen[0]['pointsTotal']
            for ind in gen:
                points += ind['pointsTotal']
                if ind['pointsTotal'] < min:
                    min = ind['pointsTotal']

                if ind['pointsTotal'] > max:
                    max = ind['pointsTotal']
            avgPoints.append(points/500)
            minPoints.append(min)
            maxPoints.append(max)
        width = 1
        xlabels = ['I', 'II', 'III', 'IV', 'V']
        worst = np.array(minPoints)
        best = np.array(maxPoints)
        values = np.array([worst, best])
        x = np.arange(values.shape[1])
        fig, ax = plt.subplots()
        spacing = 0.3  # spacing between hat groups
        width = (1 - spacing) / values.shape[0]
        heights0 = values[0]
        for i, heights in enumerate(values):
            style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
            rects = ax.bar(x - spacing / 2 + i * width, heights - heights0,
                           width, bottom=heights0, **style)
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.plot(range(len(avgPoints)),avgPoints)
        ax.legend()

        plt.show()