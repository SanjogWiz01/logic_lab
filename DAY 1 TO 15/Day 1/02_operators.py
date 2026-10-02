"""Day 1 - Arithmetic and comparison operators.

Logic concept: combining values with operators and chaining comparisons.
"""


def add(a, b):
    """Return the sum of ``a`` and ``b``."""
    return a + b


def safe_divide(a, b):
    """Return ``a / b`` or ``None`` when dividing by zero."""
    if b == 0:
        return None
    return a / b


def is_even(n):
    """Return ``True`` when ``n`` is an even integer."""
    return n % 2 == 0


def clamp(value, low, high):
    """Return ``value`` forced inside the range ``low..high``."""
    if value < low:
        return low
    if value > high:
        return high
    return value


def is_leap_year(year):
    """Return ``True`` when ``year`` is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def in_range(value, low, high):
    """Return ``True`` when ``low <= value <= high``."""
    return low <= value <= high


def max_of_three(a, b, c):
    """Return the largest of three values."""
    return max(a, b, c)


if __name__ == "__main__":
    print("add(3, 4):", add(3, 4))
    print("safe_divide(10, 2):", safe_divide(10, 2))
    print("safe_divide(10, 0):", safe_divide(10, 0))
    print("is_even(7):", is_even(7))
    print("clamp(15, 0, 10):", clamp(15, 0, 10))
    print("leap years:", [year for year in range(2000, 2024) if is_leap_year(year)])
    print("in_range(5, 1, 10):", in_range(5, 1, 10))
    print("max_of_three(4, 9, 2):", max_of_three(4, 9, 2))
