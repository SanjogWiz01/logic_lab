from functools import lru_cache


@lru_cache(maxsize=None)
def fibo(n):
    """Return the n-th Fibonacci number, starting with fibo(0) == 0."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
