def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    k=0
    for i in range(N+1):
        if i==0:
            k+=0
        else:
            k+=1/i
    return k
print(main(4))
