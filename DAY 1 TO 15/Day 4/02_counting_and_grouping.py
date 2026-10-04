"""Day 4 - Counting and grouping with dictionaries.

Logic concept: building frequency maps and collecting items per key.
"""


def char_counts(text):
    """Return how many times each character appears in ``text``."""
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def word_counts(text):
    """Return how many times each whitespace-separated word appears."""
    counts = {}
    for word in text.lower().split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def most_common(counts, top=1):
    """Return the ``top`` ``(item, count)`` pairs, biggest count first."""
    pairs = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return pairs[:top]


def first_max_key(counts):
    """Return the key with the highest count, or ``None`` when empty."""
    if not counts:
        return None
    best_key = None
    best_count = None
    for key, count in counts.items():
        if best_count is None or count > best_count:
            best_key = key
            best_count = count
    return best_key


def group_by_length(words):
    """Return a dictionary mapping word length to the words of that length."""
    groups = {}
    for word in words:
        size = len(word)
        if size not in groups:
            groups[size] = []
        groups[size].append(word)
    return groups


def group_anagrams(words):
    """Return a dictionary of anagram groups keyed by sorted letters."""
    groups = {}
    for word in words:
        signature = "".join(sorted(word.lower()))
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)
    return groups


def index_by_key(records, key):
    """Return a dictionary that maps ``key`` values to whole records."""
    lookup = {}
    for record in records:
        lookup[record[key]] = record
    return lookup


def duplicates_found(items):
    """Return the items that appear more than once, in first-seen order."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    repeated = []
    for item in items:
        if counts[item] > 1 and item not in repeated:
            repeated.append(item)
    return repeated


def running_total(numbers):
    """Return a dictionary of ``value -> running total`` up to that point."""
    totals = {}
    running = 0
    for number in numbers:
        running += number
        totals[number] = running
    return totals


if __name__ == "__main__":
    print("char_counts('mississippi'):", char_counts("mississippi"))
    print("word_counts('the cat the dog'):", word_counts("the cat the dog"))
    print("most_common(char_counts('aabbb')):", most_common(char_counts("aabbb"), 2))
    print("first_max_key({'a': 1, 'b': 5}):", first_max_key({"a": 1, "b": 5}))
    print("group_by_length(['bat', 'hi', 'ox']):", group_by_length(["bat", "hi", "ox"]))
    print(
        "group_anagrams(['eat', 'tea', 'bat']):", group_anagrams(["eat", "tea", "bat"])
    )
    records = [{"id": 1, "name": "a"}, {"id": 2, "name": "b"}]
    print("index_by_key(records, 'id'):", index_by_key(records, "id"))
    print("duplicates_found([1, 2, 2, 3, 1]):", duplicates_found([1, 2, 2, 3, 1]))
    print("running_total([1, 2, 3]):", running_total([1, 2, 3]))
