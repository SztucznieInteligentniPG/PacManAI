from __future__ import annotations
import json


from reward import Reward


class Statistic:
    data: dict

    def __init__(self):
        self.data = {
            'pointsTotal': 0,
            'points': 0,
            'powerUps': 0,
            'deaths': 0,
            'time': 0,
            'ghosts': 0,
            'pointsPoints': 0,
            'pointsPowerUps': 0,
            'pointsDeaths': 0,
            'pointsTime': 0,
            'pointsGhosts': 0}

    def addPoint(self, value: int, type: Reward):
        rewardType = Reward(type)
        if rewardType == Reward.POINT:
            self.data['points'] += 1
            self.data['pointsPoints'] += Reward.POINT.value
            self.data['pointsTotal'] += Reward.POINT.value
        elif rewardType == Reward.POWER_UP:
            self.data['powerUps'] += 1
            self.data['pointsPowerUps'] += Reward.POWER_UP.value
            self.data['pointsTotal'] += Reward.POWER_UP.value
        elif rewardType == Reward.DEATH:
            self.data['deaths'] += 1
            self.data['pointsDeaths'] += Reward.DEATH.value
            self.data['pointsTotal'] += Reward.DEATH.value
        elif rewardType == Reward.TIME_REMAINING:
            self.data['time'] += 1
            self.data['pointsTime'] += value
            self.data['pointsTotal'] += value
        elif rewardType == Reward.KILLED_GHOST:
            self.data['ghosts'] += 1
            self.data['pointsGhosts'] += value
            self.data['pointsTotal'] += value
