"""Day 2 - String building and searching.

Logic concept: accumulation, membership checks, and formatting.
"""


def capitalize_words(sentence):
    """Return ``sentence`` with every word capitalized."""
    return " ".join(word.capitalize() for word in sentence.split())


def remove_duplicates(text):
    """Return ``text`` with repeated characters collapsed."""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


def contains_all(text, required):
    """Return ``True`` when every character of ``required`` is in ``text``."""
    lowered = text.lower()
    for char in required.lower():
        if char not in lowered:
            return False
    return True


def title_case_initials(names):
    """Return the uppercase initials of each name."""
    return " ".join(name[0].upper() for name in names.split())


def swap_case(text):
    """Flip the case of every letter in ``text``."""
    return text.swapcase()


def longest_word(sentence):
    """Return the longest word in ``sentence``."""
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


if __name__ == "__main__":
    print(
        "capitalize_words('hello brave new world'):",
        capitalize_words("hello brave new world"),
    )
    print("remove_duplicates('programming'):", remove_duplicates("programming"))
    print("contains_all('keyboard', 'key'):", contains_all("keyboard", "key"))
    print("contains_all('keyboard', 'z'):", contains_all("keyboard", "z"))
    print("title_case_initials('ada lovelace'):", title_case_initials("ada lovelace"))
    print("swap_case('Logic Lab'):", swap_case("Logic Lab"))
    print("longest_word('a bb cccc dd'):", longest_word("a bb cccc dd"))
