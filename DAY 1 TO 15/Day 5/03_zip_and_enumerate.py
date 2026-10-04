"""Day 5 - zip, enumerate, and pairing collections.

Logic concept: walking several collections together with position awareness.
"""


def index_items(items):
    """Return ``(index, item)`` pairs, mirroring ``enumerate``."""
    pairs = []
    for index in range(len(items)):
        pairs.append((index, items[index]))
    return pairs


def index_items_starting_at(items, start=1):
    """Return ``(position, item)`` pairs starting the count at ``start``."""
    pairs = []
    position = start
    for item in items:
        pairs.append((position, item))
        position += 1
    return pairs


def pair_same_length(first, second):
    """Return pairs built from two equal-length collections."""
    if len(first) != len(second):
        raise ValueError("collections must be the same length")
    return [(first[index], second[index]) for index in range(len(first))]


def pair_shortest(first, second):
    """Return pairs built from the shorter of the two collections."""
    size = min(len(first), len(second))
    return [(first[index], second[index]) for index in range(size)]


def pair_longest(first, second, filler=None):
    """Return pairs covering both collections, padding with ``filler``."""
    pairs = []
    size = max(len(first), len(second))
    for index in range(size):
        left = first[index] if index < len(first) else filler
        right = second[index] if index < len(second) else filler
        pairs.append((left, right))
    return pairs


def zip_dicts(first, second):
    """Return a dictionary from two collections of keys and values."""
    return dict(zip(first, second, strict=False))


def unzip_pairs(pairs):
    """Return ``(firsts, seconds)`` split back out of a list of pairs."""
    firsts = []
    seconds = []
    for left, right in pairs:
        firsts.append(left)
        seconds.append(right)
    return (firsts, seconds)


def index_by_pair(items, key_index):
    """Return a dictionary keyed by one position of each item."""
    lookup = {}
    for item in items:
        lookup[item[key_index]] = item
    return lookup


def positions_of(items, target):
    """Return every position where ``target`` shows up."""
    found = []
    for position, item in enumerate(items):
        if item == target:
            found.append(position)
    return found


def running_pairs(numbers):
    """Return ``(previous, current)`` pairs for consecutive numbers."""
    pairs = []
    for index in range(1, len(numbers)):
        pairs.append((numbers[index - 1], numbers[index]))
    return pairs


if __name__ == "__main__":
    print("index_items(['a', 'b']):", index_items(["a", "b"]))
    print(
        "index_items_starting_at(['a', 'b'], 1):", index_items_starting_at(["a", "b"])
    )
    print("pair_same_length([1, 2], ['a', 'b']):", pair_same_length([1, 2], ["a", "b"]))
    print("pair_shortest([1, 2, 3], ['a']):", pair_shortest([1, 2, 3], ["a"]))
    print("pair_longest([1, 2], ['a'], 0):", pair_longest([1, 2], ["a"], 0))
    print("zip_dicts(['a', 'b'], [1, 2]):", zip_dicts(["a", "b"], [1, 2]))
    print("unzip_pairs([(1, 'a'), (2, 'b')]):", unzip_pairs([(1, "a"), (2, "b")]))
    rows = [("id", 1), ("id", 2)]
    print("index_by_pair(rows, 0):", index_by_pair(rows, 0))
    print("positions_of([1, 2, 1], 1):", positions_of([1, 2, 1], 1))
    print("running_pairs([1, 2, 3]):", running_pairs([1, 2, 3]))
