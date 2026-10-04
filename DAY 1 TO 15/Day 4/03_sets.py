"""Day 4 - Sets and set operations.

Logic concept: uniqueness, membership tests, and combining collections.
"""


def make_set(items):
    """Return a set holding the unique items in ``items``."""
    return set(items)


def unique_in_order(items):
    """Return a list with repeats removed but original order kept."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def common_items(first, second):
    """Return the items present in both collections."""
    return sorted(set(first) & set(second))


def only_in_first(first, second):
    """Return items in ``first`` that are missing from ``second``."""
    return sorted(set(first) - set(second))


def in_either(first, second):
    """Return the items found in either collection but not both."""
    return sorted(set(first) ^ set(second))


def in_either_or_both(first, second):
    """Return every item found in at least one collection."""
    return sorted(set(first) | set(second))


def is_subset(small, large):
    """Return ``True`` when every item of ``small`` is inside ``large``."""
    return set(small).issubset(set(large))


def is_disjoint(first, second):
    """Return ``True`` when the collections share nothing."""
    return set(first).isdisjoint(set(second))


def covers_all(small, large):
    """Return the items of ``large`` that ``small`` fails to cover."""
    return sorted(set(large) - set(small))


def split_unique(items, pivot):
    """Split ``items`` into the ones inside ``pivot`` and the ones outside."""
    inside = set(pivot)
    kept = [item for item in items if item in inside]
    dropped = [item for item in items if item not in inside]
    return unique_in_order(kept), unique_in_order(dropped)


def rotate_cycle(items, steps):
    """Return the unique items rotated left by ``steps`` positions."""
    data = unique_in_order(items)
    if not data:
        return []
    shift = steps % len(data)
    return data[shift:] + data[:shift]


if __name__ == "__main__":
    left = [1, 2, 3, 4]
    right = [3, 4, 5]
    print("make_set([1, 1, 2]):", sorted(make_set([1, 1, 2])))
    print("unique_in_order([1, 2, 1, 3]):", unique_in_order([1, 2, 1, 3]))
    print("common_items(left, right):", common_items(left, right))
    print("only_in_first(left, right):", only_in_first(left, right))
    print("in_either(left, right):", in_either(left, right))
    print("in_either_or_both(left, right):", in_either_or_both(left, right))
    print("is_subset([1, 2], left):", is_subset([1, 2], left))
    print("is_disjoint([1, 2], [3, 4]):", is_disjoint([1, 2], [3, 4]))
    print("covers_all([1], [1, 9]):", covers_all([1], [1, 9]))
    print("split_unique([1, 2, 3, 4], [4, 2]):", split_unique([1, 2, 3, 4], [4, 2]))
    print("rotate_cycle([1, 2, 3, 4, 5], 2):", rotate_cycle([1, 2, 3, 4, 5], 2))
