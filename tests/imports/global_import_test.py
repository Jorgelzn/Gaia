import genoforge


def test_global_import():
    assert genoforge.metrics.semantic.levenshtein_distance("test","test") == 0