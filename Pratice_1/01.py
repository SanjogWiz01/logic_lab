"""
Write a function is_prime(n) that returns True if a number is prime.
Then use it to print all primes between 1 and 100.
"""


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # check divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter a number to check: "))
    result = "is" if is_prime(num) else "is not"
    print(f"{num} {result} a prime number.")
