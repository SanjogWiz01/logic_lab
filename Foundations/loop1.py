"""Small factorial practice exercise."""


def factorial(n):
    """Return ``n!`` for a non-negative integer."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


# Keep the original exercise runnable without prompting during imports.
funct = factorial


if __name__ == "__main__":
    print(factorial(int(input("Enter a number for its factorial: "))))
