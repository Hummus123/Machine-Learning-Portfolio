# This is practice with config classes as well as doing Monte Carlo simulations in one line in two ways.
#
#

import random
import math
import numpy as np


class config():
    def __init__(self, n = 99999):
        self.n = n

config = config(n = 10000)
Monte1 = len([1 for truth, truth2 in zip([random.random() for i in range(config.n)],[random.random() for i in range(config.n)]) if truth**2 + truth2**2 <= 1]) / config.n * 4
Monte2 = sum(np.array([random.random() for i in range(config.n)])**2 + np.array([random.random() for i in range(config.n)])**2 <= 1) / config.n * 4
truth_array = np.array([random.random() for i in range(config.n)])**2 + np.array([random.random()] * config.n)**2 <= 1
print(Monte1)
print(Monte2)
print(truth_array)
print((f"{Monte2=}"))
