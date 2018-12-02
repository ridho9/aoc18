from functools import reduce

with open('input') as f:
    res = reduce(lambda x, y: x + y, (int(x) for x in f.readlines()))
    print(res)
