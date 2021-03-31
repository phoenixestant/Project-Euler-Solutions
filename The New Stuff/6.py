# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 2640.
# Find the difference between the sum of the 
# squares of the first one hundred natural numbers and the square of the sum.

# two fns sum of squares, square of sums
# subtract sq of sums from sum of sqs

def sum_of_squares(array):
    return sum([i**2 for i in array])

def square_of_sums(array):
    return sum(array)**2


def b(a):
    sum(a)

def main():
    first_ten = range(1, 101)
    #print(sum_of_squares(first_ten))
    print(abs(square_of_sums(first_ten) - sum_of_squares(first_ten)))

    # sqs = get_sq
    # sums = get_sums()
    # print(sums - sqs)


if __name__ == '__main__':
    main()