import json
from matplotlib import pyplot as plt
import pandas as pd

from src.reward import Reward
from statistic import Statistic
from tracker import Tracker

def createPieChart():
        tracker = Tracker('statistics/2021-05-29_22_50_27')
        tracker.load()
        points = 0
        powerUps = 0
        ghosts = 0
        time = 0
        for gen in tracker.data:
                for ind in gen:
                        points += ind['pointsPoints']
                        powerUps += ind['pointsPowerUps']
                        ghosts += ind['pointsGhosts']
                        time += ind['pointsTime']

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        labels = ['Points', 'PowerUps', 'Time', 'Ghosts']
        students = [points,powerUps,time,ghosts]
        ax.pie(students, labels=labels, autopct='%1.2f%%')
        plt.show()
if __name__ == '__main__':
    createPieChart()
