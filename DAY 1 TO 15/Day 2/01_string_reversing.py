"""Day 2 - Reversing and rotating strings.

Logic concept: swapping, two pointers, and index walking.
"""


def reverse_string(text):
    """Return ``text`` reversed."""
    return text[::-1]


def reverse_words(text):
    """Return the words of ``text`` in reverse order."""
    return " ".join(text.split()[::-1])


def is_palindrome(text):
    """Return ``True`` when ``text`` reads the same both ways."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def two_pointer_reverse(characters):
    """Reverse a list in place using two pointers."""
    left = 0
    right = len(characters) - 1
    while left < right:
        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1
    return characters


def rotate(text, steps):
    """Return ``text`` rotated left by ``steps`` characters."""
    if not text:
        return text
    steps %= len(text)
    return text[steps:] + text[:steps]


def longest_run(characters):
    """Return the longest run of the same character."""
    best = run = 1
    for index in range(1, len(characters)):
        if characters[index] == characters[index - 1]:
            run += 1
        else:
            run = 1
        best = max(best, run)
    return best


if __name__ == "__main__":
    print("reverse_string('logic'):", reverse_string("logic"))
    print("reverse_words('the quick brown fox'):", reverse_words("the quick brown fox"))
    print("is_palindrome('Race car'):", is_palindrome("Race car"))
    print("is_palindrome('python'):", is_palindrome("python"))
    print("two_pointer_reverse:", two_pointer_reverse(["a", "b", "c", "d", "e"]))
    print("rotate('abcdef', 2):", rotate("abcdef", 2))
    print("rotate('abcdef', 8):", rotate("abcdef", 8))
    print("longest_run('aaabbcddd'):", longest_run("aaabbcddd"))
