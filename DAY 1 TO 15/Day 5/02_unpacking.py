"""Day 5 - Unpacking and assignment.

Logic concept: binding several values at once and swapping without temp files.
"""


def split_pair(pair):
    """Return ``(first, second)`` taken from a two-item sequence."""
    first, second = pair
    return (first, second)


def swap_values(first, second):
    """Return the two values exchanged."""
    return (second, first)


def sum_and_product(numbers):
    """Return ``(total, product)`` for ``numbers``."""
    total = 0
    product = 1
    for number in numbers:
        total += number
        product *= number
    return (total, product)


def head_and_tail(items):
    """Return ``(first_item, remaining_items)`` for ``items``."""
    data = list(items)
    if not data:
        return (None, [])
    return (data[0], data[1:])


def collect_heads(groups):
    """Return the first item of every group."""
    heads = []
    for group in groups:
        first, *_rest = group
        heads.append(first)
    return heads


def starred_middle(items):
    """Return ``(first, middle, last)`` using star unpacking."""
    first, *middle, last = items
    return (first, middle, last)


def nested_unpack(record):
    """Pull a name and city out of ``((name, age), city)``."""
    (name, _age), city = record
    return (name, city)


def unpack_to_dict(names, values):
    """Return a dictionary built by zipping names with values."""
    return dict(zip(names, values, strict=True))


def swap_in_place(items, first_index, second_index):
    """Return a copy of ``items`` with two positions exchanged."""
    data = list(items)
    data[first_index], data[second_index] = data[second_index], data[first_index]
    return data


def compare_pairs(first, second):
    """Return ``-1``, ``0``, or ``1`` comparing two-item sequences."""
    left = tuple(first)
    right = tuple(second)
    if left < right:
        return -1
    if left > right:
        return 1
    return 0


if __name__ == "__main__":
    print("split_pair((1, 'a')):", split_pair((1, "a")))
    print("swap_values(1, 2):", swap_values(1, 2))
    print("sum_and_product([1, 2, 3, 4]):", sum_and_product([1, 2, 3, 4]))
    print("head_and_tail([7, 8, 9]):", head_and_tail([7, 8, 9]))
    print("collect_heads([[1, 2], [3]]):", collect_heads([[1, 2], [3]]))
    print("starred_middle([1, 2, 3, 4]):", starred_middle([1, 2, 3, 4]))
    print(
        "nested_unpack((('Asha', 24), 'Pune')):", nested_unpack((("Asha", 24), "Pune"))
    )
    print("unpack_to_dict(['a', 'b'], [1, 2]):", unpack_to_dict(["a", "b"], [1, 2]))
    print("swap_in_place([1, 2, 3], 0, 2):", swap_in_place([1, 2, 3], 0, 2))
    print("compare_pairs([1, 2], [1, 3]):", compare_pairs([1, 2], [1, 3]))
