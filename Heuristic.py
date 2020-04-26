import Vector
import numpy as np


def heuristic(current, goal, D):
    dx = abs(goal.x - current.x)
    dy = abs(goal.y - current.y)
    return D*np.sqrt(dx**2 + dy**2)




