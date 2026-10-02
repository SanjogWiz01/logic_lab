"""Day 1 - Loops and accumulators.

Logic concept: running totals, break, continue, and while loops.
"""


def sum_range(start, end):
    """Return the sum of every integer from ``start`` to ``end`` inclusive."""
    total = 0
    for value in range(start, end + 1):
        total += value
    return total


def count_divisors(n):
    """Return how many positive divisors ``n`` has."""
    if n <= 0:
        raise ValueError("n must be positive")
    count = 0
    for candidate in range(1, int(n**0.5) + 1):
        if n % candidate == 0:
            count += 2 if candidate * candidate != n else 1
    return count


def first_divisible(values, target):
    """Return the first value divisible by ``target``, or ``None``."""
    for value in values:
        if value % target == 0:
            return value
    return None


def skip_and_stop(values):
    """Return values before the first negative, ignoring values below 2."""
    kept = []
    for value in values:
        if value < 0:
            break
        if value < 2:
            continue
        kept.append(value)
    return kept


def digit_count(n):
    """Return the number of digits in ``n`` using a while loop."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


if __name__ == "__main__":
    print("sum_range(1, 10):", sum_range(1, 10))
    print("sum_range(5, 5):", sum_range(5, 5))
    for n in [1, 12, 16, 28, 97]:
        print(f"divisors of {n}: {count_divisors(n)}")
    print("first_divisible([3, 7, 10, 12], 5):", first_divisible([3, 7, 10, 12], 5))
    print("skip_and_stop([1, 5, -3, 9]):", skip_and_stop([1, 5, -3, 9]))
    print("digit_count(0):", digit_count(0))
    print("digit_count(918273):", digit_count(918273))
