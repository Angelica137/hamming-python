from scripts.hamming import hamming_distance
import pytest


def test_hamming_distance_empty_strings():
    assert hamming_distance("", "") == 0


def test_hamming_distance_longer_strings():
    assert hamming_distance("abc", "abc") == 0


def test_hamming_distance_one_difference():
    assert hamming_distance("abc", "abd") == 1


def test_hamming_distance_7_differences():
    assert hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7


def test_hamming_distance_different_lengths():
    with pytest.raises(ValueError):
        hamming_distance("abc", "abcd") == ValueError(
            "Strands must be of equal length.")
