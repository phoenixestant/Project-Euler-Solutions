# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#NOTES
# we only want prime factors
# so it has to be a factor
# and that factor has to be prime
# we want largest

# use the test case

import math

def factors_of(a):
    """Returns a list of factors of a"""
    factors=[]
    for g in range(3, round(math.sqrt(a)), 2):
        if is_factor(g,a):
            factors.append(g)
    return(factors)


def is_factor(a, b):
    """Returns true if a is a factor of b
    e.g. 3 is a factor of 12, thus True"""
    return b % a == 0

def primes_of(list_):
    array = []
    for i in list_:
        if is_prime(i):
            array.append(i)
    return array
    
def is_prime(r):
    # if r % 1 and % r only, return true
    if 1 < r < 4:
        return True
    for i in range(3, round(math.sqrt(r)), 2):
        if r % i == 0:
            return False
    return True

def main():
    input_ = 600851475143
    factors = factors_of(input_)
    primes = primes_of(factors)
    answer = max(primes)
    print(answer)


if __name__ == '__main__':
    main()
