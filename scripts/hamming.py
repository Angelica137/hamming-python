def hamming_distance(a: str, b: str) -> int:
    """
    Calculates and returns the number of differences in two DNA strands
    """
    if len(a) != len(b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
