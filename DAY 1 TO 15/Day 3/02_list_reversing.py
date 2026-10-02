"""Day 3 - Reversing and rotating lists.

Logic concept: swapping in place versus building a new list.
"""


def reverse_list(items):
    """Return a new list with the elements in reverse order."""
    return items[::-1]


def reverse_in_place(items):
    """Reverse ``items`` using two pointers and return it."""
    left = 0
    right = len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items


def rotate(items, steps):
    """Return ``items`` rotated left by ``steps`` positions."""
    if not items:
        return []
    steps %= len(items)
    return items[steps:] + items[:steps]


def reverse_groups(items, size):
    """Reverse each chunk of ``size`` items in place."""
    for start in range(0, len(items), size):
        end = start + size - 1
        left = start
        right = min(end, len(items) - 1)
        while left < right:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1
    return items


def palindrome_list(items):
    """Return ``True`` when the list reads the same in both directions."""
    if len(items) < 2:
        return True
    left = 0
    right = len(items) - 1
    while left < right:
        if items[left] != items[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print("reverse_list([1, 2, 3, 4]):", reverse_list([1, 2, 3, 4]))
    print("reverse_in_place:", reverse_in_place(["a", "b", "c"]))
    print("rotate([1, 2, 3, 4, 5], 2):", rotate([1, 2, 3, 4, 5], 2))
    print("rotate([1, 2, 3], 4):", rotate([1, 2, 3], 4))
    print("reverse_groups([1, 2, 3, 4, 5], 2):", reverse_groups([1, 2, 3, 4, 5], 2))
    print("palindrome_list([1, 2, 1]):", palindrome_list([1, 2, 1]))
    print("palindrome_list([1, 2, 3]):", palindrome_list([1, 2, 3]))
