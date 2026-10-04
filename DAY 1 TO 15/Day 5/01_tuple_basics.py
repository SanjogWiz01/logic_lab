"""Day 5 - Tuple basics.

Logic concept: fixed-length groups, indexing, slicing, and immutability.
"""


def make_point(x, y):
    """Return a tuple holding one point."""
    return (x, y)


def first_and_last(items):
    """Return the first and last item of ``items`` as a tuple."""
    if not items:
        return (None, None)
    return (items[0], items[-1])


def swap_ends(items):
    """Return a tuple with the ends of ``items`` exchanged."""
    data = tuple(items)
    if len(data) < 2:
        return data
    return (data[-1],) + data[1:-1] + (data[0],)


def rotate_tuple(items, steps):
    """Return ``items`` rotated left by ``steps`` positions."""
    data = tuple(items)
    if not data:
        return ()
    shift = steps % len(data)
    return data[shift:] + data[:shift]


def middle_slice(items):
    """Return the tuple without its first and last item."""
    data = tuple(items)
    return data[1:-1]


def tuple_to_list(items):
    """Return a mutable list copy of ``items``."""
    return list(items)


def clamp_pair(pair, low, high):
    """Return the pair with each value kept inside ``low`` and ``high``."""
    return tuple(min(high, max(low, value)) for value in pair)


def pair_up(first, second):
    """Return tuples that pair each item of ``first`` with ``second``."""
    size = min(len(first), len(second))
    return tuple((first[index], second[index]) for index in range(size))


def distance_manhattan(first, second):
    """Return the Manhattan distance between two points."""
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def is_palindrome_tuple(items):
    """Return ``True`` when the tuple reads the same both ways."""
    data = tuple(items)
    return data == data[::-1]


if __name__ == "__main__":
    print("make_point(2, 3):", make_point(2, 3))
    print("first_and_last([4, 5, 6]):", first_and_last([4, 5, 6]))
    print("first_and_last([]):", first_and_last([]))
    print("swap_ends([1, 2, 3, 4]):", swap_ends([1, 2, 3, 4]))
    print("rotate_tuple((1, 2, 3, 4), 1):", rotate_tuple((1, 2, 3, 4), 1))
    print("middle_slice((1, 2, 3, 4)):", middle_slice((1, 2, 3, 4)))
    print("tuple_to_list((1, 2)):", tuple_to_list((1, 2)))
    print("clamp_pair((-5, 12), 0, 10):", clamp_pair((-5, 12), 0, 10))
    print("pair_up([1, 2, 3], ['a', 'b']):", pair_up([1, 2, 3], ["a", "b"]))
    print("distance_manhattan((0, 0), (3, 4)):", distance_manhattan((0, 0), (3, 4)))
    print("is_palindrome_tuple((1, 2, 1)):", is_palindrome_tuple((1, 2, 1)))
