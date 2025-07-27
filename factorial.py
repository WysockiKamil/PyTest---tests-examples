def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Podana musi być liczba całkowita")
    if n < 0:
        raise ValueError("Podana musi być liczba nieujemna")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result