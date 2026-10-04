"""Day 6 - Backtracking.

Logic concept: try a choice, explore it, then undo it before the next try.
"""


def all_subsets(items):
    """Return every subset of ``items``, each as a list."""
    return build_subsets(list(items), 0, [])


def build_subsets(items, index, current):
    """Grow a subset one item at a time and backtrack afterwards."""
    if index == len(items):
        return [current]
    without = build_subsets(items, index + 1, current)
    with_item = build_subsets(items, index + 1, current + [items[index]])
    return without + with_item


def all_permutations(items):
    """Return every ordering of ``items``."""
    return build_permutations(list(items), [])


def build_permutations(remaining, current):
    """Pick one remaining item, recurse, then remove it again."""
    if not remaining:
        return [current]
    results = []
    for position in range(len(remaining)):
        chosen = remaining[position]
        rest = remaining[:position] + remaining[position + 1 :]
        for tail in build_permutations(rest, current + [chosen]):
            results.append(tail)
    return results


def permutations_of_size(items, size):
    """Return every ordering of ``size`` items taken from ``items``."""
    return build_sized(list(items), [], size)


def build_sized(remaining, current, size):
    """Fill the current ordering up to ``size`` then stop."""
    if len(current) == size:
        return [current]
    results = []
    for position in range(len(remaining)):
        chosen = remaining[position]
        rest = remaining[:position] + remaining[position + 1 :]
        results.extend(build_sized(rest, current + [chosen], size))
    return results


def combinations(items, size):
    """Return every group of ``size`` items taken in original order."""
    return build_combinations(list(items), 0, [], size)


def build_combinations(items, start, current, size):
    """Skip or take each item while keeping the original order."""
    if len(current) == size:
        return [current]
    results = []
    for index in range(start, len(items)):
        results.extend(
            build_combinations(items, index + 1, current + [items[index]], size)
        )
    return results


def word_exists(board, word):
    """Return ``True`` when ``word`` can be spelled on ``board``."""
    return search_word(board, word, 0, 0, set())


def search_word(board, word, row, column, visited):
    """Walk to neighbouring cells, marking each one as used."""
    if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
        return False
    if (row, column) in visited:
        return False
    if board[row][column] != word[0]:
        return False
    if len(word) == 1:
        return True
    visited.add((row, column))
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row_step, column_step in steps:
        if search_word(board, word[1:], row + row_step, column + column_step, visited):
            return True
    visited.remove((row, column))
    return False


if __name__ == "__main__":
    print("all_subsets([1, 2]):", sorted(all_subsets([1, 2]), key=len))
    print("all_permutations([1, 2, 3]):", all_permutations([1, 2, 3]))
    print("permutations_of_size([1, 2, 3], 2):", permutations_of_size([1, 2, 3], 2))
    print("combinations([1, 2, 3], 2):", combinations([1, 2, 3], 2))
    grid = [["A", "B"], ["C", "D"]]
    print("word_exists(grid, 'AB'):", word_exists(grid, "AB"))
    print("word_exists(grid, 'AC'):", word_exists(grid, "AC"))
    print("word_exists(grid, 'AD'):", word_exists(grid, "AD"))
