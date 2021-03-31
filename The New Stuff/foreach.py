def test():
    l = [1, 2, 3]

    def add(a, b):
        return a + b

    def is_odd(a, *args):
        return a % 2 == 1

    def double(a, *args):
        return a * 2

    def print_item(i):
        print(i)

    # test for_each - expect
    # 1
    # 2
    # 3
    for_each(l, print_item)

    # test map
    print(map_(l, double) == [2, 4, 6])
    # test filter
    print(filter_(l, is_odd) == [1, 3])
    # test fold
    # print(fold(l, add, 0) == 6)


if __name__ == "__main__":
    test()