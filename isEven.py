def isEven(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Argument must be a number")

    if n % 2 == 0:
        return True
    else:
        return False

