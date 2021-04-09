import one

def denominators(numerator):
    return [denominator for denominator in range(1,numerator + 1) if numerator % denominator == 0]

def filter_divisors(denominators, divisor):
    return [number for number in denominators if number % divisor == 0]