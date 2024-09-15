import random
from genoforge import fitness
def test_add():
    assert fitness.add(1, 2) == 3
    assert fitness.add(0.1, 3) == 3.1
    a, b = random.random(), random.random()
    assert fitness.add(a, b) == a + b