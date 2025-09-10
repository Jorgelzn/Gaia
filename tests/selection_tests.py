import numpy as np
from gaia import selection

def test_tournamet():
    def check(number: int):
        return number/10

    population = selection.tournament.tournament_without_replacement(np.array([1, 2, 3, 4, 5]), 2, check)

    print(population)

