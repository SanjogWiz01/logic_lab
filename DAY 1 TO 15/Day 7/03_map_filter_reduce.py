"""Day 7 - map, filter, and reduce style pipelines.

Logic concept: chaining small transformations instead of one big loop.
"""

from functools import reduce


def double_each(numbers):
    """Return each number doubled."""
    return list(map(lambda number: number * 2, numbers))


def absolute_values(numbers):
    """Return each number turned into its absolute value."""
    return list(map(abs, numbers))


def keep_even(numbers):
    """Return only the even numbers."""
    return list(filter(lambda number: number % 2 == 0, numbers))


def keep_long_words(words, minimum=4):
    """Return only the words reaching ``minimum`` characters."""
    return list(filter(lambda word: len(word) >= minimum, words))


def total_of(numbers):
    """Return the sum of ``numbers``."""
    return reduce(lambda running, number: running + number, numbers, 0)


def product_of(numbers):
    """Return the product of ``numbers``."""
    return reduce(lambda running, number: running * number, numbers, 1)


def longest_word(words):
    """Return the longest word, or ``None`` when there are none."""
    data = list(words)
    if not data:
        return None
    return reduce(lambda best, word: word if len(word) > len(best) else best, data)


def apply_pipeline(numbers):
    """Return the doubled values of the even numbers only."""
    return list(
        map(lambda number: number * 2, filter(lambda number: number % 2 == 0, numbers))
    )


def running_totals(numbers):
    """Return the running total after each number."""
    totals = []
    running = 0
    for number in numbers:
        running += number
        totals.append(running)
    return totals


def average_of(numbers):
    """Return the mean of ``numbers``, or ``0.0`` when empty."""
    data = list(numbers)
    if not data:
        return 0.0
    return total_of(data) / len(data)


def any_negative(numbers):
    """Return ``True`` when at least one number is below zero."""
    return any(number < 0 for number in numbers)


def all_even(numbers):
    """Return ``True`` when every number is even."""
    return all(number % 2 == 0 for number in numbers)


if __name__ == "__main__":
    print("double_each([1, 2, 3]):", double_each([1, 2, 3]))
    print("absolute_values([-3, 4]):", absolute_values([-3, 4]))
    print("keep_even([1, 2, 3, 4]):", keep_even([1, 2, 3, 4]))
    print("keep_long_words(['a', 'logic'], 4):", keep_long_words(["a", "logic"]))
    print("total_of([1, 2, 3]):", total_of([1, 2, 3]))
    print("product_of([1, 2, 3, 4]):", product_of([1, 2, 3, 4]))
    print("longest_word(['a', 'logic', 'lab']):", longest_word(["a", "logic", "lab"]))
    print("apply_pipeline([1, 2, 3, 4]):", apply_pipeline([1, 2, 3, 4]))
    print("running_totals([1, 2, 3]):", running_totals([1, 2, 3]))
    print("average_of([2, 4]):", average_of([2, 4]))
    print("any_negative([1, -1]):", any_negative([1, -1]))
    print("all_even([2, 4, 6]):", all_even([2, 4, 6]))
