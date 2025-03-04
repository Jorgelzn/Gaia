from genoforge import metrics


def test_module_import():
    assert metrics.semantic.levenshtein_distance("test", "test") == 0
