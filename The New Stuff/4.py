# A palindromic number reads the same both ways. T
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def get_all_the_numbers():
    min_ = 100
    max_ = 1000
    all_the_numbers = []
    for i in range (min_, max_):
        for j in range (min_, max_):
            all_the_numbers.append(i*j)
    return all_the_numbers


def is_palindrome(num):
    string = str(num)
    return string == string[::-1]

def main():
    nums = get_all_the_numbers()
    palindromes = [num for num in nums if is_palindrome(num)]
    print(max(palindromes))


if __name__ == '__main__':
    main()