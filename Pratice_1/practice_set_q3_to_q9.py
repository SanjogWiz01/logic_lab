"""Practice set solutions for questions 3 to 9."""


def two_sum(nums, target):
    """Return indices of the first pair whose values add up to target."""
    seen = {}

    for index, number in enumerate(nums):
        needed = target - number

        if needed in seen:
            return [seen[needed], index]

        seen[number] = index

    return []


def flatten_deep(nested):
    """Flatten a list nested to any depth."""
    flattened = []

    for item in nested:
        if isinstance(item, list):
            flattened.extend(flatten_deep(item))
        else:
            flattened.append(item)

    return flattened


def group_anagrams(words):
    """Group words that contain the same letters."""
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


def binary_search(arr, target):
    """Return target index in a sorted list, or -1 when not found."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def most_frequent(lst):
    """Return the most frequent item without Counter or max(key=...)."""
    if not lst:
        return None

    counts = {}
    best_item = lst[0]
    best_count = 0

    for item in lst:
        if item not in counts:
            counts[item] = 0

        counts[item] += 1

        if counts[item] > best_count:
            best_count = counts[item]
            best_item = item

    return best_item


def rotate_matrix(matrix):
    """Rotate a 3x3 matrix 90 degrees clockwise in-place."""
    size = 3

    for row in range(size):
        for col in range(row + 1, size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def pascal_triangle(n):
    """Print the first n rows of Pascal's Triangle."""
    row = []

    for row_number in range(n):
        next_row = []

        for index in range(row_number + 1):
            if index == 0 or index == row_number:
                next_row.append(1)
            else:
                next_row.append(row[index - 1] + row[index])

        print(next_row)
        row = next_row


if __name__ == "__main__":
    print("Q3 two_sum:")
    print(two_sum([2, 7, 11, 15], 9))

    print("\nQ4 flatten_deep:")
    print(flatten_deep([[1, [2, 3]], [4, [5, [6]]]]))

    print("\nQ5 group_anagrams:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    print("\nQ6 binary_search:")
    print(binary_search([1, 3, 5, 7, 9], 7))
    print(binary_search([1, 3, 5, 7, 9], 4))

    print("\nQ7 most_frequent:")
    print(most_frequent([1, 2, 2, 3, 3, 3, 4]))

    print("\nQ8 rotate_matrix:")
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("Before:")
    print_matrix(sample_matrix)
    rotate_matrix(sample_matrix)
    print("After:")
    print_matrix(sample_matrix)

    print("\nQ9 pascal_triangle:")
    pascal_triangle(5)
