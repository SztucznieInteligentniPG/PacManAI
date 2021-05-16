from enum import Enum


class Reward(Enum):
    POINT = 1
    POWER_UP = 5
    DEATH = -20
    TIME_REMAINING = 3
    KILLED_GHOST = 10
