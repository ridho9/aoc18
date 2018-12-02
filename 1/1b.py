from itertools import cycle

res = 0
found = set([0])

with open('input') as f:
    for n in cycle(f.readlines()):
        res += int(n)
        if res in found:
            print(res)
            break
        found.add(res)
