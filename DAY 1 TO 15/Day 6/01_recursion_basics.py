"""Day 6 - Recursion basics.

Logic concept: base cases, shrinking inputs, and letting calls return answers.
"""


def factorial(n):
    """Return ``n!`` using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_to(n):
    """Return the sum of every integer from 1 to ``n``."""
    if n <= 0:
        return 0
    return n + sum_to(n - 1)


def countdown(n):
    """Return the numbers from ``n`` down to 1."""
    if n <= 0:
        return []
    return [n] + countdown(n - 1)


def fib(n):
    """Return the ``n``-th Fibonacci number, counting ``fib(0)`` as 0."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def power(base, exponent):
    """Return ``base`` raised to ``exponent``."""
    if exponent == 0:
        return 1
    if exponent < 0:
        raise ValueError("exponent must not be negative")
    return base * power(base, exponent - 1)


def digit_sum(n):
    """Return the sum of the digits of ``n``."""
    if n < 0:
        return digit_sum(-n)
    if n < 10:
        return n
    return digit_sum(n // 10) + n % 10


def is_palindrome_number(n):
    """Return ``True`` when ``n`` reads the same in both directions."""
    if n < 0:
        return False
    if n < 10:
        return True
    left = n
    right = 0
    while left > 0:
        right = right * 10 + left % 10
        left //= 10
    return right == n


def greatest_common_divisor(first, second):
    """Return the GCD using the recursive Euclidean step."""
    if second == 0:
        return abs(first)
    return greatest_common_divisor(second, first % second)


if __name__ == "__main__":
    print("factorial(5):", factorial(5))
    print("sum_to(5):", sum_to(5))
    print("countdown(4):", countdown(4))
    print("fib(7):", fib(7))
    print("power(2, 10):", power(2, 10))
    print("digit_sum(9182):", digit_sum(9182))
    print("is_palindrome_number(121):", is_palindrome_number(121))
    print("is_palindrome_number(123):", is_palindrome_number(123))
    print("greatest_common_divisor(48, 18):", greatest_common_divisor(48, 18))
