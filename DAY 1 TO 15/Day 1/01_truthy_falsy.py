"""Day 1 - Truthiness and falsy values.

Logic concept: deciding *whether a value counts as true* without an
explicit comparison.
"""


def is_truthy(value):
    """Return ``True`` when Python treats ``value`` as true."""
    return bool(value)


def describe(value):
    """Return a short label explaining why ``value`` is true or false."""
    return "truthy" if is_truthy(value) else "falsy"


def falsy_values():
    """Return the values that Python considers false."""
    return [0, 0.0, "", [], {}, set(), None, False]


def count_truthy(values):
    """Return how many items in ``values`` are truthy."""
    total = 0
    for value in values:
        if is_truthy(value):
            total += 1
    return total


def first_truthy(values):
    """Return the first truthy item, or ``None`` when there is none."""
    for value in values:
        if is_truthy(value):
            return value
    return None


if __name__ == "__main__":
    print("Falsy values:", falsy_values())
    print(
        "count_truthy([0, '', 5, None, [], 'hi']):",
        count_truthy([0, "", 5, None, [], "hi"]),
    )
    print("first_truthy([0, None, 'found', 9]):", first_truthy([0, None, "found", 9]))

    for sample in [0, 1, "", "text", [], [0], None, {}, {"a": 1}]:
        print(f"{sample!r:12} -> {describe(sample)}")
