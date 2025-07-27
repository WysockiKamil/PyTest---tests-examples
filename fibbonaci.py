def fibbonaci(n):
    if not isinstance(n, int):
        raise TypeError("Podana musi być liczba całkowita")
    if n < 0:
        raise ValueError("Podana musi być liczba nieujemna")
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a
