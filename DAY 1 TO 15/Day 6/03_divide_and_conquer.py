"""Day 6 - Divide and conquer.

Logic concept: cutting a problem in half and trusting the smaller answers.
"""


def recursive_binary_search(sorted_items, target):
    """Return the index of ``target`` in a sorted list, or ``-1``."""
    return search_range(sorted_items, target, 0, len(sorted_items) - 1)


def search_range(sorted_items, target, low, high):
    """Binary search restricted to the ``low``-``high`` window."""
    if low > high:
        return -1
    middle = (low + high) // 2
    value = sorted_items[middle]
    if value == target:
        return middle
    if value < target:
        return search_range(sorted_items, target, middle + 1, high)
    return search_range(sorted_items, target, low, middle - 1)


def merge(left, right):
    """Return two sorted lists merged into one sorted list."""
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(numbers):
    """Return a sorted copy of ``numbers`` using recursive merge sort."""
    data = list(numbers)
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def sum_range(low, high):
    """Return the sum of every integer from ``low`` to ``high`` inclusive."""
    if low > high:
        return 0
    if low == high:
        return low
    middle = (low + high) // 2
    return sum_range(low, middle) + sum_range(middle + 1, high)


def count_divisors(n):
    """Return how many positive divisors ``n`` has."""
    if n <= 0:
        raise ValueError("n must be positive")
    return count_up_to(n, 1, int(n**0.5))


def count_up_to(n, low, high):
    """Count divisor pairs of ``n`` between ``low`` and ``high``."""
    if low > high:
        return 0
    if low == high:
        if n % low != 0:
            return 0
        return 1 if low * low == n else 2
    middle = (low + high) // 2
    return count_up_to(n, low, middle) + count_up_to(n, middle + 1, high)


def count_pairs_with_sum(sorted_items, target):
    """Return how many pairs in a sorted list add up to ``target``."""
    return count_pairs_range(sorted_items, target, 0, len(sorted_items) - 1)


def count_pairs_range(sorted_items, target, low, high):
    """Walk the two ends of the window until the pointers cross."""
    if low >= high:
        return 0
    total = sorted_items[low] + sorted_items[high]
    if total == target:
        return 1 + count_pairs_range(sorted_items, target, low + 1, high - 1)
    if total < target:
        return count_pairs_range(sorted_items, target, low + 1, high)
    return count_pairs_range(sorted_items, target, low, high - 1)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print("recursive_binary_search(numbers, 7):", recursive_binary_search(numbers, 7))
    print("recursive_binary_search(numbers, 4):", recursive_binary_search(numbers, 4))
    print("merge([1, 4], [2, 3]):", merge([1, 4], [2, 3]))
    print("merge_sort(numbers):", merge_sort(numbers))
    print("sum_range(1, 10):", sum_range(1, 10))
    print("count_divisors(28):", count_divisors(28))
    print("count_divisors(97):", count_divisors(97))
    print(
        "count_pairs_with_sum([1, 2, 3, 4, 5], 7):",
        count_pairs_with_sum([1, 2, 3, 4, 5], 7),
    )
    print(
        "count_pairs_with_sum([1, 2, 3, 4, 5], 11):",
        count_pairs_with_sum([1, 2, 3, 4, 5], 11),
    )
