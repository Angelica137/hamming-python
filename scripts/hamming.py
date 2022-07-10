def hamming_distance(a: str, b: str) -> int:
    """
    Calculates and returns the number of differences in two DNA strands
    """
    if len(a) != len(b):
        raise ValueError("Strands must be of equal length.")
    return sum(a[i] != b[i] for i in range(len(a)))
