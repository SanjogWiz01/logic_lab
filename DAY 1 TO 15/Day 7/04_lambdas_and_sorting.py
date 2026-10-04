"""Day 7 - Lambdas, sorting keys, and small callbacks.

Logic concept: passing behaviour into a function so it can be reused.
"""


def apply_twice(function, value):
    """Return ``function(function(value))``."""
    return function(function(value))


def make_adder(amount):
    """Return a function that adds ``amount`` to its argument."""

    def adder(value):
        return value + amount

    return adder


def sort_numbers_by(numbers, reverse=False):
    """Return numbers ordered from smallest to largest."""
    return sorted(numbers, reverse=reverse)


def sort_by_length(words):
    """Return words ordered by length, shortest first."""
    return sorted(words, key=len)


def sort_records_by(records, position=1, reverse=False):
    """Return ``(name, value)`` records ordered by one position."""
    return sorted(records, key=lambda record: record[position], reverse=reverse)


def sort_by_second_letter(words):
    """Return words ordered by their second character."""

    def second_letter(word):
        return word[1] if len(word) > 1 else ""

    return sorted(words, key=second_letter)


def pick(items, condition):
    """Return the items that satisfy ``condition``."""
    kept = []
    for item in items:
        if condition(item):
            kept.append(item)
    return kept


def transform(items, function):
    """Return ``function`` applied to every item."""
    results = []
    for item in items:
        results.append(function(item))
    return results


def compose_functions(first, second):
    """Return a function that applies ``second`` then ``first``."""

    def combined(value):
        return first(second(value))

    return combined


def top_n(items, count):
    """Return the ``count`` largest items."""
    return sorted(items, reverse=True)[:count]


if __name__ == "__main__":
    print("apply_twice(abs, -3):", apply_twice(abs, -3))
    print("make_adder(10)(5):", make_adder(10)(5))
    print("sort_numbers_by([3, 1, 2]):", sort_numbers_by([3, 1, 2]))
    print("sort_by_length(['ccc', 'a', 'bb']):", sort_by_length(["ccc", "a", "bb"]))
    rows = [("Asha", 72), ("Bala", 91)]
    print("sort_records_by(rows):", sort_records_by(rows))
    print(
        "sort_by_second_letter(['ab', 'ba', 'ac']):",
        sort_by_second_letter(["ab", "ba", "ac"]),
    )
    print(
        "pick([1, 2, 3, 4], lambda n: n % 2 == 0):",
        pick([1, 2, 3, 4], lambda n: n % 2 == 0),
    )
    print("transform([1, 2], lambda n: n + 1):", transform([1, 2], lambda n: n + 1))
    print(
        "compose_functions(abs, lambda n: -n)(-4):",
        compose_functions(abs, lambda n: -n)(-4),
    )
    print("top_n([4, 9, 1, 7], 2):", top_n([4, 9, 1, 7], 2))
