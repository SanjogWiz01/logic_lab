"""Day 4 - Dictionary basics.

Logic concept: key/value lookup, safe access, and updating stored values.
"""


def make_profile(name, age, city):
    """Return a dictionary describing one person."""
    return {"name": name, "age": age, "city": city}


def get_value(record, key, fallback=None):
    """Return ``record[key]``, or ``fallback`` when the key is missing."""
    return record.get(key, fallback)


def add_or_update(record, key, value):
    """Return a copy of ``record`` with ``key`` set to ``value``."""
    updated = dict(record)
    updated[key] = value
    return updated


def increment(record, key, step=1):
    """Return a copy of ``record`` with a numeric counter increased."""
    updated = dict(record)
    updated[key] = updated.get(key, 0) + step
    return updated


def merge_records(first, second):
    """Return one dictionary; values from ``second`` win on conflict."""
    merged = dict(first)
    merged.update(second)
    return merged


def keys_above(record, limit):
    """Return the keys whose values are greater than ``limit``."""
    return [key for key, value in record.items() if value > limit]


def rename_key(record, old_key, new_key):
    """Return a copy of ``record`` with ``old_key`` moved to ``new_key``."""
    if old_key not in record:
        return dict(record)
    updated = {}
    for key, value in record.items():
        if key == old_key:
            updated[new_key] = value
        else:
            updated[key] = value
    return updated


def drop_key(record, key):
    """Return a copy of ``record`` without ``key``."""
    updated = dict(record)
    updated.pop(key, None)
    return updated


def invert(record):
    """Return a new dictionary that swaps every key with its value."""
    return {value: key for key, value in record.items()}


def sort_by_value(record, reverse=False):
    """Return ``(key, value)`` pairs ordered by value."""
    return sorted(record.items(), key=lambda pair: pair[1], reverse=reverse)


if __name__ == "__main__":
    profile = make_profile("Asha", 24, "Pune")
    print("profile:", profile)
    print("get_value(profile, 'city'):", get_value(profile, "city"))
    print("get_value(profile, 'pin', 'unknown'):", get_value(profile, "pin", "unknown"))
    print("add_or_update(profile, 'age', 25):", add_or_update(profile, "age", 25))
    print("increment({}, 'views'):", increment({}, "views"))
    print("increment({'views': 4}, 'views', 3):", increment({"views": 4}, "views", 3))
    print(
        "merge_records({'a': 1}, {'a': 9, 'b': 2}):",
        merge_records({"a": 1}, {"a": 9, "b": 2}),
    )
    print("rename_key(profile, 'city', 'town'):", rename_key(profile, "city", "town"))
    print("drop_key(profile, 'age'):", drop_key(profile, "age"))
    print("invert({'a': 1, 'b': 2}):", invert({"a": 1, "b": 2}))
    print("sort_by_value({'a': 3, 'b': 1}):", sort_by_value({"a": 3, "b": 1}))
