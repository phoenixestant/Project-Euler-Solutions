# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def is_multiple(numerator,denominator):
    if numerator % denominator == 0:
        return True

def sums_of_multiples(min_,max_,divisor_1,divisor_2):
    return sum([number for number in range(min_, max_) if is_multiple(number,divisor_1) or is_multiple(number,divisor_2)])
    
if __name__ == "__main__":
    print(sums_of_multiples(1,1000,3,5))