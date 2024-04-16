def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    k=0
    for i in range(A,B):
        k+=i
    return k
print(main(3,6))