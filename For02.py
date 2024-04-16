def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    answer=""
    for i in range(n):
        answer+=f"{i},"
    return answer[:-1]
print(main(3))