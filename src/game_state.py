from enum import Enum

class GameState(Enum):
    RUNNING = 0
    RUNNING_CHAOS = 1
    WON = 2
    LOST = 3
    RESPAWNING = 4
