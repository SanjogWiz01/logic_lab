"""Day 2 - Splitting, joining, and slicing strings.

Logic concept: tokenizing text and working with slices.
"""


def split_sentences(text):
    """Split ``text`` into a list of trimmed, non-empty sentences."""
    sentences = []
    for chunk in text.replace("!", ".").replace("?", ".").split("."):
        cleaned = chunk.strip()
        if cleaned:
            sentences.append(cleaned)
    return sentences


def join_with(items, separator=", "):
    """Join ``items`` into a single string using ``separator``."""
    return separator.join(str(item) for item in items)


def every_nth(items, step):
    """Return every ``step``-th item starting from the first."""
    if step <= 0:
        raise ValueError("step must be positive")
    return list(items[::step])


def chunk_string(text, size):
    """Split ``text`` into chunks of at most ``size`` characters."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [text[index : index + size] for index in range(0, len(text), size)]


def between(text, start_marker, end_marker):
    """Return the text between two markers, or ``None`` when not found."""
    start = text.find(start_marker)
    if start == -1:
        return None
    start += len(start_marker)
    end = text.find(end_marker, start)
    if end == -1:
        return None
    return text[start:end]


def truncate(text, limit):
    """Shorten ``text`` to ``limit`` characters with an ellipsis."""
    if limit <= 0:
        raise ValueError("limit must be positive")
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)] + "..."


if __name__ == "__main__":
    text = "First one. Second one! Third one? Ignored  "
    print("split_sentences:", split_sentences(text))
    print("join_with(['a', 1, True]):", join_with(["a", 1, True]))
    print("every_nth('abcdefgh', 3):", every_nth("abcdefgh", 3))
    print("chunk_string('abcdefgh', 3):", chunk_string("abcdefgh", 3))
    print("between('key=value;', 'key=', ';'):", between("key=value;", "key=", ";"))
    print("between('key=value', 'key=', ';'):", between("key=value", "key=", ";"))
    print("truncate('logic lab daily', 12):", truncate("logic lab daily", 12))
