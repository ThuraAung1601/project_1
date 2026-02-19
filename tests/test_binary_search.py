from src.binary_search import binary_search


def test_finds_value_in_middle():
    data = [-5, -1, 0, 3, 9, 13]
    assert binary_search(data, 3) == 3


def test_returns_minus_one_when_missing():
    assert binary_search([1, 2, 4, 8], 3) == -1


def test_handles_empty_sequence():
    assert binary_search([], 42) == -1


def test_handles_duplicates():
    data = [1, 2, 2, 2, 5]
    idx = binary_search(data, 2)
    assert data[idx] == 2


def test_supports_non_numeric_comparables():
    animals = ["ant", "bee", "cat", "dog"]
    assert binary_search(animals, "bee") == 1
