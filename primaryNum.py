def isPrimary(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Argument must be a number")

    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True