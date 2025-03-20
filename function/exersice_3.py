def is_prime_number(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Example usage
number = 1
if is_prime_number(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
