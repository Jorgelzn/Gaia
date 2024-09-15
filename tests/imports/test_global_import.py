import genoforge

def test_global_import():
    assert genoforge.fitness.rest(1, 2) == -1
    assert genoforge.fitness.Fitness.add(1, 2) == 3