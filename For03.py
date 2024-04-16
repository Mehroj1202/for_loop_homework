def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    answer=[]
    for i in range(n):
        answer.append(k)
    return answer
print(main(5,3))
print(main(-1,4))
