# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def is_multiple(numerator,denominator):
    if numerator % denominator == 0:
        return True

def multiples(numerator):
    return [denominator for denominator in range(1,numerator + 1) if numerator % denominator == 0]
   
print(multiples(30))
