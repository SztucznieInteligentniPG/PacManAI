from enum import Enum

class GameState(Enum):
    RUNNING = 0
    RUNNING_CHAOS = 1
    PSYCHODELIC = 2
    WON = 3
    LOST = 4
    RESPAWNING = 5
