
# Define a function called 'for_each' that takes a list: 'list_' and a function: 'fn'
# Iterate over the list calling the function on each item

def for_each(list_, fn):
    for y in list_:
        fn(y)
             
             
def fold(list_, fn, current_item=None):
    if current_item is None:
        current_item = list_[0]
    for next_item in list_:
        current_item = fn(next_item, current_item)
    return current_item

def product(list_):
    return fold(list_, multiply)

def sum_(list_):
    return fold(list_, add)

def add(a, b):
    return a + b

def min_(list_):
    return fold(list_, lesser)

def lesser(a, b):
    return a if a < b else b





def max_(list_):
    return fold(list_, greater)

def greater(a,b):
    return a if a > b else b



def multiply(a, b):
    return a * b

# Define a function called 'map_' that takes a list: 'list_' and a function: 'fn'
# Return a new list containing the result of calling the function on each item in the list
def map_(list_, fn):
    return [fn(g) for g in list_]
    #list_2 = []
    #for g in list_:
    #    list_2.append(fn(g))
    #return list_2

# Define a function called 'filter_' that takes a list: 'list_' and a function: 'fn'
# Return a new list containing only the items in the original list that return True when calling the function on the item
def filter_(list_, fn):
    #return [fn(item == True) for item in list_]
    list_3 = []
    for item in list_:
        if fn(item) == True:
            list_3.append(item)
    return list_3

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

    # test min_ expect 1
    print(min_([1, 2, 3]) == 1)
    
    # test min_ expect -3
    print(min_([-1, -2, -3]) == -3)

    # test max_ expect 5
    print(max_([1,2,3,4,5]) == 5)

    # test max_ expect 5
    print(max_([-1,-2,-3,-4,-5]) == -1)

if __name__ == "__main__":
    test()