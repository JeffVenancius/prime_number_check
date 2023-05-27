import math

# this algorithm has many aproaches, each one more complex than the previous.
# the idea is to discover if the number is not a prime with the less calculations possible.

# let's say the input is between 1 and 1000:
# - The first aproach checks if the number is even, if it is then it's not a prime.
# 490 numbers dealed, 510 to go.
# - Second checks if the square root is an integer, more 15 numbers.
# - Third we take the rounded square root and get the prime factors between, notice that we only need the square. 
# As even numbers are dealt with, you don't need to get the number 2 either.
# Now finally we check if input % == factor 0 with a Lazy aproach.
# if none of these aproaches were enough, then it must be a prime.


def get_factor(min, max):
# As we just want to get prime numbers here, we do easy_is_not_prime each loop and avoid some ones.
    for i in range(min + 1, max + 1):
        if easy_is_not_prime(i):
            continue
        i_prime = True
        for j in range(i, max):
            if i % j == 0:
                i_prime = False
                break
        if i_prime:
            return i
    return 0 # Falsy.


def easy_is_not_prime(value):
    if value != 2 and not value & 1: # binary operation to check if it's even.
        return True
    sqrt_value = math.sqrt(value) 
    if sqrt_value == round(sqrt_value):
        return True
    return False


def is_prime(input):
    if easy_is_not_prime(input):
        return False
# Lazy aproach
    factor = 3
    rounded = round(math.sqrt(input))
    while factor:
        if input % factor == 0:
            return False
        factor = get_factor(factor, rounded)
    return True

# Test
for i in range (0, 10000):
    if is_prime(i):
        print(i)
