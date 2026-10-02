"""Day 3 - Nested lists and running totals.

Logic concept: flattening, aggregating, and matrix traversal.
"""


def flatten(nested):
    """Return a flat list containing every number from ``nested``."""
    flat = []
    for group in nested:
        if isinstance(group, list):
            flat.extend(flatten(group))
        else:
            flat.append(group)
    return flat


def total(nested):
    """Return the sum of every number inside ``nested``."""
    running = 0
    for value in flatten(nested):
        running += value
    return running


def row_totals(matrix):
    """Return the sum of each row in ``matrix``."""
    return [sum(row) for row in matrix]


def column_totals(matrix):
    """Return the sum of each column in ``matrix``."""
    if not matrix:
        return []
    columns = len(matrix[0])
    return [sum(row[index] for row in matrix) for index in range(columns)]


def transpose(matrix):
    """Return the rows and columns of ``matrix`` swapped."""
    if not matrix:
        return []
    return [list(column) for column in zip(*matrix, strict=True)]


def max_subarray(numbers):
    """Return the largest sum obtainable from a contiguous slice."""
    if not numbers:
        return 0
    best = current = numbers[0]
    for value in numbers[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best


if __name__ == "__main__":
    nested = [1, [2, [3, 4]], 5]
    print("flatten:", flatten(nested))
    print("total:", total(nested))
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    print("row_totals:", row_totals(matrix))
    print("column_totals:", column_totals(matrix))
    print("transpose:", transpose(matrix))
    print(
        "max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]):",
        max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
    )
