import numpy as np


class RandomPlayer():
    @staticmethod
    def play(n):
        randomvalue = np.random.randint(n)

        return randomvalue