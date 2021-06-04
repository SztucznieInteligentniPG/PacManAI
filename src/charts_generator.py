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
            for ind in gen['population']:
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
            for ind in gen['population']:
                sum += ind['deaths']
            deathCount.append(sum / gen['population'].__len__())

        X = range(1, deathCount.__len__() + 1)
        z = np.polyfit(X, deathCount, 10)
        p = np.poly1d(z)

        plt.plot(X,p(X),"b--")
        plt.plot(X,deathCount,'r')
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
            for ind in gen['population']:
                points += ind['pointsPoints'] + ind['pointsPowerUps'] + ind['pointsGhosts'] + ind['pointsTime']
                powerUps += ind['pointsPowerUps'] + ind['pointsGhosts'] + ind['pointsTime']
                ghosts += ind['pointsGhosts'] + ind['pointsTime']
                time += ind['pointsTime']
            pointsData.append(points/gen['population'].__len__())
            powerUpsData.append(powerUps/gen['population'].__len__())
            ghostsData.append(ghosts/gen['population'].__len__())
            timeData.append(time/gen['population'].__len__())
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
            min = gen['population'][0]['pointsTotal']
            max = gen['population'][0]['pointsTotal']
            for ind in gen['population']:
                points += ind['pointsTotal']
                if ind['pointsTotal'] < min:
                    min = ind['pointsTotal']

                if ind['pointsTotal'] > max:
                    max = ind['pointsTotal']
            avgPoints.append(points/gen['population'].__len__())
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
            style = {'fill': False} if i == 0 else {'edgecolor': 'lightgreen'}
            rects = ax.bar(x - spacing / 2 + i * width, heights - heights0,
                           width, bottom=heights0, **style)
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.plot(range(len(avgPoints)),avgPoints)
        ax.legend()

        plt.show()