"""Day 7 - List comprehensions.

Logic concept: building a new list from an old one in a single expression.
"""


def square_each(numbers):
    """Return a list with every number squared."""
    return [number * number for number in numbers]


def keep_positive(numbers):
    """Return only the values greater than zero."""
    return [number for number in numbers if number > 0]


def squares_of_range(size):
    """Return the squares of the numbers from 0 up to ``size`` - 1."""
    return [number * number for number in range(size)]


def flatten(nested):
    """Return one flat list built from a list of lists."""
    return [value for group in nested for value in group]


def scale_pairs(numbers, factors):
    """Return each number multiplied by its matching factor."""
    return [number * factor for number, factor in zip(numbers, factors, strict=False)]


def words_longer_than(words, minimum):
    """Return the words longer than ``minimum`` characters."""
    return [word for word in words if len(word) > minimum]


def pair_with_index(items):
    """Return ``(index, item)`` pairs as a list of tuples."""
    return [(index, item) for index, item in enumerate(items)]


def running_totals(numbers):
    """Return the running total after each number."""
    totals = []
    running = 0
    for number in numbers:
        running += number
        totals.append(running)
    return totals


def rotate_list(items, steps):
    """Return ``items`` rotated left by ``steps`` positions."""
    data = list(items)
    if not data:
        return []
    shift = steps % len(data)
    return data[shift:] + data[:shift]


if __name__ == "__main__":
    print("square_each([1, 2, 3]):", square_each([1, 2, 3]))
    print("keep_positive([-2, 0, 5]):", keep_positive([-2, 0, 5]))
    print("squares_of_range(5):", squares_of_range(5))
    print("flatten([[1, 2], [3]]):", flatten([[1, 2], [3]]))
    print("scale_pairs([1, 2], [10, 20]):", scale_pairs([1, 2], [10, 20]))
    print("words_longer_than(['a', 'bee'], 1):", words_longer_than(["a", "bee"], 1))
    print("pair_with_index(['a', 'b']):", pair_with_index(["a", "b"]))
    print("running_totals([1, 2, 3]):", running_totals([1, 2, 3]))
    print("rotate_list([1, 2, 3, 4], 2):", rotate_list([1, 2, 3, 4], 2))
