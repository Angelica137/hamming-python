def hamming_distance(a: str, b: str) -> int:
    """
    Calculates and returns the number of differences in two DNA strands
    """
    if a == b:
        return 0
