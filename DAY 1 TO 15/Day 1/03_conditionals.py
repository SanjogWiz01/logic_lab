"""Day 1 - Conditional branching.

Logic concept: if / elif / else, early returns, and nested decisions.
"""


def grade(score):
    """Return a letter grade for a score between 0 and 100."""
    if not 0 <= score <= 100:
        return "invalid"
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 40:
        return "D"
    return "F"


def is_positive_even(n):
    """Return ``True`` when ``n`` is both positive and even."""
    if n <= 0:
        return False
    return n % 2 == 0


def absolute_value(n):
    """Return the magnitude of ``n``."""
    if n < 0:
        return -n
    return n


def describe_number(n):
    """Describe ``n`` with early-return branches."""
    if n == 0:
        return "zero"
    if n > 0:
        if n % 2 == 0:
            return "positive even"
        return "positive odd"
    if n % 2 == 0:
        return "negative even"
    return "negative odd"


def fizzbuzz(n):
    """Return the FizzBuzz label for a single number."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


if __name__ == "__main__":
    for score in [95, 80, 65, 45, 12, 120]:
        print(f"score {score:4} -> {grade(score)}")

    for n in [0, 7, -4, -9]:
        print(f"{n:3} -> {describe_number(n)}")

    print("is_positive_even(8):", is_positive_even(8))
    print("is_positive_even(-8):", is_positive_even(-8))
    print("absolute_value(-13):", absolute_value(-13))
    print("fizzbuzz 1-20:", [fizzbuzz(n) for n in range(1, 21)])
