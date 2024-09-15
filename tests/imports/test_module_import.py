from genoforge import fitness
import genoforge.fitness
def test_module_import():
    assert fitness.rest(1, 2) == -1
    assert fitness.Fitness.add(1, 2) == 3
    assert genoforge.fitness.rest(1, 2) == -1