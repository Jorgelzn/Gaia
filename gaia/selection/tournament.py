import numpy as np


def tournament_without_replacement(population: np.ndarray, selective_pressure: int,fitness: callable):

    parents = np.empty(population.shape, int)

    for parent_idx in range(len(parents)):
        fighters = population[np.random.choice(population.shape[0], selective_pressure, replace=False)]
        fighters_values = np.array([fitness(fighter) for fighter in fighters])
        parents[parent_idx] = fighters[np.argmin(fighters_values)]

    return parents