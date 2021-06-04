from __future__ import annotations
import json


from statistic import Statistic


class Tracker:
    data: list
    #fileName : string nie ma w annotations?

    def __init__(self, fileName):
        self.data = []
        self.fileName = fileName

    def setGeneration(self, statisticList: list[Statistic], generationNumber: int, seed: int):
        generation = {"seed": seed, "population": []}
        for i in range(statisticList.__len__()):
            stats = statisticList[i]
            generation["population"].append(stats.data)

        if generationNumber < len(self.data):
            self.data[generationNumber] = generation
        else:
            self.data.append(generation)

    def load(self):
        f = open(self.fileName, "r")
        self.data = json.load(f)

    def saveData(self):
        with open(self.fileName, 'w') as outfile:
            json.dump(self.data, outfile)

