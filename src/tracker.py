from __future__ import annotations
import json


from statistic import Statistic


class Tracker:
    data: list
    genCounter: int
    #fileName : string nie ma w annotations?

    def __init__(self, fileName):
        self.genCounter = 0
        self.data = []
        self.fileName = fileName

    def setGeneration(self, statisticList: list[Statistic], generationNumber: int):

        generacja = []
        for i in range(statisticList.__len__()):
            stats = statisticList[i]
            generacja.append(stats.data)
        if generationNumber >= self.genCounter:
            self.genCounter += 1
            self.data[generationNumber] = generacja
        else:
            self.data.append(generacja)

    def load(self):
        f = open(self.fileName, "r")
        self.data = json.load(f)

    def saveData(self):
        with open(self.fileName, 'w') as outfile:
            json.dump(self.data, outfile)

