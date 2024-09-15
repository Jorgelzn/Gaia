from genoforge.fitness import Fitness,rest

def test_local_import():
    assert rest(1, 2) == -1
    assert Fitness.add(1, 2) == 3