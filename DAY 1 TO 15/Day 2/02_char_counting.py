"""Day 2 - Counting characters in a string.

Logic concept: frequency maps built with dictionaries.
"""


def char_counts(text):
    """Return a mapping of character to occurrence count."""
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def most_common_char(text):
    """Return the most frequent character, or ``None`` for empty input."""
    counts = char_counts(text)
    if not counts:
        return None
    best_char = None
    best_count = -1
    for char, count in counts.items():
        if count > best_count:
            best_char = char
            best_count = count
    return best_char


def is_anagram(first, second):
    """Return ``True`` when both strings use the same letters."""
    return char_counts(first.lower()) == char_counts(second.lower())


def duplicates(text):
    """Return the sorted characters that appear more than once."""
    counts = char_counts(text.lower())
    return sorted(char for char, count in counts.items() if count > 1)


def word_lengths(sentence):
    """Return a mapping of word to its length."""
    return {word: len(word) for word in sentence.split()}


if __name__ == "__main__":
    text = "mississippi river"
    print("char_counts:", char_counts(text))
    print("most_common_char:", most_common_char(text))
    print("is_anagram('listen', 'silent'):", is_anagram("listen", "silent"))
    print("is_anagram('hello', 'world'):", is_anagram("hello", "world"))
    print("duplicates:", duplicates(text))
    print("word_lengths:", word_lengths("the quick brown fox"))
