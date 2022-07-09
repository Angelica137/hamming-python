from scripts.hamming import hamming_distance


def test_hamming_distance_empty_strings():
    assert hamming_distance("", "") == 0


def test_hamming_distance_longer_strings():
    assert hamming_distance("abc", "abc") == 0
