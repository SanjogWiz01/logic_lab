''' Write a function is_prime(n) that returns True if a number is prime. Then use it to print all primes between 1 and 100.'''
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

# Example usage:
print(" ENTER A NUMBER TO CHECK IF IT IS PRIME OR NOT: ")
num=int(input( ".."))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

