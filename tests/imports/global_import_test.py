import gaia


def test_global_import():
    assert gaia.metrics.semantic.levenshtein_distance("test","test") == 0