from __future__ import annotations
import json


from reward import Reward


class Statistic:
    data: dict

    def __init__(self):
        self.data = {
            'total': 0,
            'points': 0,
            'powerUps': 0,
            'deaths': 0,
            'time': 0,
            'ghosts': 0}

    def addPoint(self, value: int, type: Reward):
        rewardType = Reward(type)
        if rewardType == Reward.POINT:
            self.data['points'] += Reward.POINT.value
            self.data['total'] += Reward.POINT.value
        elif rewardType == Reward.POWER_UP:
            self.data['powerUps'] += Reward.POWER_UP.value
            self.data['total'] += Reward.POWER_UP.value
        elif rewardType == Reward.DEATH:
            self.data['deaths'] += Reward.DEATH.value
            self.data['total'] += Reward.DEATH.value
        elif rewardType == Reward.TIME_REMAINING:
            self.data['time'] += value
            self.data['total'] += value
        elif rewardType == Reward.KILLED_GHOST:
            self.data['ghosts'] += value
            self.data['total'] += value
