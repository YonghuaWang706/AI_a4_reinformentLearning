from enum import Enum


class Agent:
    def move(self):
        pass

    def pick_start_location(self):
        pass


class Action(Enum):
    up = 1
    down = 2
    left = 3
    right = 4
