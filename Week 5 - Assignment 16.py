


'''
Challenge: Optimize the function to handle large input numbers efficiently.

=====================================================
Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise.
'''

import math

def is_prime(n):
    # Handle small cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check factors up to sqrt(n) using 6k ± 1 rule
    limit = int(math.sqrt(n)) + 1
    i = 5

    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
