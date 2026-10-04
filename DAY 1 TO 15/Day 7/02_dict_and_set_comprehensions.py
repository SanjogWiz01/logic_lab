"""Day 7 - Dict and set comprehensions.

Logic concept: building mappings and unique collections in one expression.
"""


def index_of_each(items):
    """Return ``item -> position`` for every item."""
    return {item: index for index, item in enumerate(items)}


def counts_of(items):
    """Return ``item -> how many times it appears``."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def unique_items(items):
    """Return the unique items as a set."""
    return {item for item in items}


def lengths_of(words):
    """Return ``word -> length`` for every word."""
    return {word: len(word) for word in words}


def invert(record):
    """Return a dictionary with every key and value exchanged."""
    return {value: key for key, value in record.items()}


def keep_big_values(record, limit):
    """Return only the entries whose value is at least ``limit``."""
    return {key: value for key, value in record.items() if value >= limit}


def group_by_length(words):
    """Return ``length -> words of that length`` built in one expression."""
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


def characters_in(text):
    """Return the set of characters used in ``text``, ignoring spaces."""
    return {char for char in text if not char.isspace()}


def squares_to_dict(size):
    """Return ``number -> number squared`` for the first ``size`` numbers."""
    return {number: number * number for number in range(size)}


def duplicates(items):
    """Return a set of the items that appear more than once."""
    counts = counts_of(items)
    return {item for item, count in counts.items() if count > 1}


if __name__ == "__main__":
    print("index_of_each(['a', 'b', 'a']):", index_of_each(["a", "b", "a"]))
    print("counts_of([1, 2, 2, 3]):", counts_of([1, 2, 2, 3]))
    print("unique_items([1, 1, 2]):", sorted(unique_items([1, 1, 2])))
    print("lengths_of(['bat', 'hi']):", lengths_of(["bat", "hi"]))
    print("invert({'a': 1}):", invert({"a": 1}))
    print("keep_big_values({'a': 1, 'b': 5}, 5):", keep_big_values({"a": 1, "b": 5}, 5))
    print("group_by_length(['bat', 'hi', 'ox']):", group_by_length(["bat", "hi", "ox"]))
    print("characters_in('a b'):", sorted(characters_in("a b")))
    print("squares_to_dict(4):", squares_to_dict(4))
    print("duplicates([1, 2, 2, 3]):", sorted(duplicates([1, 2, 2, 3])))
