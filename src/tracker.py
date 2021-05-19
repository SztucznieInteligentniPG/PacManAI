from __future__ import annotations
import json


from statistic import Statistic


class Tracker:
    data: dict
    genCounter: int
    #fileName : string nie ma w annotations?

    def __init__(self, fileName):
        self.genCounter = 0
        self.data = {}
        self.fileName = fileName

    def addGeneration(self, statisticList: list[Statistic]):
        name = 'gen'+str(self.genCounter)
        self.data[name] = []
        for i in range(statisticList.__len__()):
            self.data[name]['ind'+str(i)] = Statistic(statisticList[i]).data
        self.genCounter += 1





    def saveData(self):
        with open(self.fileName, 'w') as outfile:
            json.dump(self.data, outfile)

