"""Day 3 - Searching inside lists.

Logic concept: linear scan, bounds checks, and early exits.
"""


def find_index(items, target):
    """Return the index of ``target``, or ``-1`` when it is absent."""
    for index in range(len(items)):
        if items[index] == target:
            return index
    return -1


def contains(items, target):
    """Return ``True`` when ``target`` is in ``items``."""
    return find_index(items, target) != -1


def find_all_indices(items, target):
    """Return every index where ``target`` appears."""
    indices = []
    for index, value in enumerate(items):
        if value == target:
            indices.append(index)
    return indices


def find_maximum(items):
    """Return the largest item, or ``None`` for an empty list."""
    if not items:
        return None
    best = items[0]
    for value in items[1:]:
        if value > best:
            best = value
    return best


def has_duplicates(items):
    """Return ``True`` when any item repeats."""
    seen = set()
    for value in items:
        if value in seen:
            return True
        seen.add(value)
    return False


def binary_search(sorted_items, target):
    """Return the index of ``target`` in a sorted list, or ``-1``."""
    low = 0
    high = len(sorted_items) - 1
    while low <= high:
        middle = (low + high) // 2
        value = sorted_items[middle]
        if value == target:
            return middle
        if value < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


if __name__ == "__main__":
    numbers = [4, 9, 15, 22, 31, 47, 58]
    print("find_index(numbers, 22):", find_index(numbers, 22))
    print("find_index(numbers, 99):", find_index(numbers, 99))
    print("contains(numbers, 31):", contains(numbers, 31))
    print("find_all_indices([1, 2, 1, 3, 1], 1):", find_all_indices([1, 2, 1, 3, 1], 1))
    print("find_maximum(numbers):", find_maximum(numbers))
    print("find_maximum([]):", find_maximum([]))
    print("has_duplicates([1, 2, 3]):", has_duplicates([1, 2, 3]))
    print("has_duplicates([1, 2, 1]):", has_duplicates([1, 2, 1]))
    print("binary_search(numbers, 47):", binary_search(numbers, 47))
    print("binary_search(numbers, 50):", binary_search(numbers, 50))
