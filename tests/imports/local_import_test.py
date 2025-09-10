from gaia.metrics.semantic import levenshtein_distance


def test_local_import():
    assert levenshtein_distance("test", "test") == 0
