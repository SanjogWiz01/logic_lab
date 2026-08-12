def ascending_stars(n):
    """Return an ascending star pattern as a list of lines."""
    _validate_size(n)
    return ["*" * width for width in range(1, n + 1)]


def descending_stars(n):
    """Return a descending star pattern as a list of lines."""
    _validate_size(n)
    return ["*" * width for width in range(n, 0, -1)]


def _validate_size(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")


if __name__ == "__main__":
    size = int(input("Enter the pattern size: "))
    print("Normal pattern")
    print("\n".join(ascending_stars(size)))
    print("Descending pattern")
    print("\n".join(descending_stars(size)))
