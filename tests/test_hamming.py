from scripts.hamming import hamming_distance


def test_hamming_distance_empty_strings():
    assert hamming_distance("", "") == 0
