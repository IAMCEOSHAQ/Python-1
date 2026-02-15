


'''
Challenge: Handle negative exponents efficiently.

====================================
Description: Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
'''

def power(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    for _ in range(exponent):
        result *= base

    return result

print(power(-3, -2))