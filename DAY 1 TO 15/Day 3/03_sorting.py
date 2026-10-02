"""Day 3 - Sorting logic.

Logic concept: comparison, swaps, and implementing simple sorts by hand.
"""


def bubble_sort(numbers):
    """Return a sorted copy of ``numbers`` using bubble sort."""
    data = list(numbers)
    for end in range(len(data) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                swapped = True
        if not swapped:
            break
    return data


def selection_sort(numbers):
    """Return a sorted copy of ``numbers`` using selection sort."""
    data = list(numbers)
    for position in range(len(data)):
        smallest = position
        for candidate in range(position + 1, len(data)):
            if data[candidate] < data[smallest]:
                smallest = candidate
        if smallest != position:
            data[position], data[smallest] = data[smallest], data[position]
    return data


def is_sorted(numbers):
    """Return ``True`` when the list is in ascending order."""
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[index - 1]:
            return False
    return True


def second_largest(numbers):
    """Return the second largest distinct value, or ``None``."""
    unique = sorted(set(numbers))
    if len(unique) < 2:
        return None
    return unique[-2]


if __name__ == "__main__":
    sample = [5, 3, 9, 1, 7, 3]
    print("bubble_sort:", bubble_sort(sample))
    print("selection_sort:", selection_sort(sample))
    print("built-in sorted:", sorted(sample))
    print("is_sorted([1, 2, 3]):", is_sorted([1, 2, 3]))
    print("is_sorted([3, 1]):", is_sorted([3, 1]))
    print("second_largest([5, 3, 9, 1, 9]):", second_largest([5, 3, 9, 1, 9]))
    print("second_largest([4, 4, 4]):", second_largest([4, 4, 4]))
