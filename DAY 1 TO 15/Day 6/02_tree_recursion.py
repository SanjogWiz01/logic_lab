"""Day 6 - Recursion over nested structures.

Logic concept: applying one rule at every level until a base case appears.
"""


def flatten(nested):
    """Return one flat list containing every value inside ``nested``."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def nested_total(nested):
    """Return the sum of every number inside ``nested``."""
    running = 0
    for value in flatten(nested):
        running += value
    return running


def nested_depth(nested):
    """Return how many list levels ``nested`` contains."""
    deepest = 0
    for item in nested:
        if isinstance(item, list):
            deepest = max(deepest, 1 + nested_depth(item))
    return deepest


def count_leaves(nested):
    """Return how many non-list values sit inside ``nested``."""
    leaves = 0
    for item in nested:
        if isinstance(item, list):
            leaves += count_leaves(item)
        else:
            leaves += 1
    return leaves


def nested_max(nested):
    """Return the largest number inside ``nested``."""
    values = flatten(nested)
    if not values:
        return None
    return max(values)


def tree_paths(nested, prefix=""):
    """Return the dotted path of every leaf inside ``nested``."""
    paths = []
    for index, item in enumerate(nested):
        label = f"{prefix}{index}"
        if isinstance(item, list):
            paths.extend(tree_paths(item, f"{label}."))
        else:
            paths.append(f"{label}={item}")
    return paths


def contains(nested, target):
    """Return ``True`` when ``target`` appears anywhere inside ``nested``."""
    for item in nested:
        if isinstance(item, list):
            if contains(item, target):
                return True
        elif item == target:
            return True
    return False


def level_widths(nested):
    """Return how many values sit at each level of ``nested``."""
    if not nested:
        return [0]
    top = [item for item in nested if not isinstance(item, list)]
    rest = [item for item in nested if isinstance(item, list)]
    widths = [len(top)]
    for item in rest:
        widths.extend(level_widths(item))
    return widths


if __name__ == "__main__":
    tree = [1, [2, [3, 4]], 5]
    print("flatten(tree):", flatten(tree))
    print("nested_total(tree):", nested_total(tree))
    print("nested_depth(tree):", nested_depth(tree))
    print("count_leaves(tree):", count_leaves(tree))
    print("nested_max(tree):", nested_max(tree))
    print("tree_paths(tree):", tree_paths(tree))
    print("contains(tree, 4):", contains(tree, 4))
    print("contains(tree, 9):", contains(tree, 9))
    print("level_widths(tree):", level_widths(tree))
