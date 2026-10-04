"""Day 4 - Combining dictionaries and sets.

Logic concept: merging mappings, swapping keys, and multi-source counting.
"""


def deep_merge(first, second):
    """Return one dictionary, merging nested dictionaries recursively."""
    merged = dict(first)
    for key, value in second.items():
        current = merged.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            merged[key] = deep_merge(current, value)
        else:
            merged[key] = value
    return merged


def flatten_record(record, prefix=""):
    """Return a flat dictionary of dotted key paths for nested records."""
    flat = {}
    for key, value in record.items():
        path = f"{prefix}{key}"
        if isinstance(value, dict):
            flat.update(flatten_record(value, f"{path}."))
        else:
            flat[path] = value
    return flat


def count_by_key(records, key):
    """Return how many records share each value of ``key``."""
    counts = {}
    for record in records:
        value = record[key]
        counts[value] = counts.get(value, 0) + 1
    return counts


def keys_used_by_all(records, key):
    """Return the values of ``key`` that every record contains."""
    if not records:
        return set()
    shared = None
    for record in records:
        values = {record[key]}
        shared = values if shared is None else shared & values
    return shared or set()


def swap_keys_and_values(record):
    """Return a dictionary with keys and values exchanged."""
    return {value: key for key, value in record.items()}


def top_values(record, count):
    """Return the ``count`` highest ``(key, value)`` pairs."""
    pairs = sorted(record.items(), key=lambda pair: pair[1], reverse=True)
    return pairs[:count]


def values_below(record, limit):
    """Return a dictionary keeping only entries under ``limit``."""
    return {key: value for key, value in record.items() if value < limit}


def shared_keys(first, second):
    """Return the sorted keys present in both dictionaries."""
    return sorted(set(first) & set(second))


if __name__ == "__main__":
    left = {"a": {"x": 1}, "b": 2}
    right = {"a": {"y": 3}}
    print("deep_merge(left, right):", deep_merge(left, right))
    nested = {"user": {"name": "Asha", "pin": {"code": 411}}}
    print("flatten_record(nested):", flatten_record(nested))
    rows = [{"dept": "eng", "name": "a"}, {"dept": "ops", "name": "b"}]
    print("count_by_key(rows, 'dept'):", count_by_key(rows, "dept"))
    print("keys_used_by_all(rows, 'dept'):", sorted(keys_used_by_all(rows, "dept")))
    print("swap_keys_and_values({'a': 1}):", swap_keys_and_values({"a": 1}))
    scores = {"a": 10, "b": 30, "c": 20}
    print("top_values(scores, 2):", top_values(scores, 2))
    print("values_below(scores, 25):", values_below(scores, 25))
    print(
        "shared_keys({'a': 1, 'b': 2}, {'b': 0, 'c': 3}):",
        shared_keys({"a": 1, "b": 2}, {"b": 0, "c": 3}),
    )
