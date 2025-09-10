from gaia.metrics import semantic


def test_sub_module_import():
    assert semantic.levenshtein_distance("test", "test") == 0