from collections import defaultdict
from functools import reduce


def count(word):
    c = defaultdict(int)
    for letter in word:
        c[letter] += 1

    have = {2: False, 3: False}

    for k in c:
        have[2] = have[2] or (c[k] == 2)
        have[3] = have[3] or (c[k] == 3)

    return (1 if have[2] else 0, 1 if have[3] else 0)


with open("input") as f:
    def r(x, y):
        v = count(y)
        return (x[0] + v[0], x[1] + v[1])
    res = reduce(r, f, (0, 0))
    print(res[0] * res[1])
