import sys
from collections import defaultdict


def parse(s):
    split = s.split()
    id = int(split[0][1:])
    c, r = [int(x) for x in split[2][:-1].split(',')]
    w, h = [int(x) for x in split[3].split('x')]
    return (r, c, w, h, id)


fabric = defaultdict(int)
claims = []


for l in sys.stdin:
    l = parse(l.strip())
    claims.append(l)

    for r in range(l[0], l[0] + l[3]):
        for c in range(l[1], l[1] + l[2]):
            fabric[(r, c)] += 1

count = 0
for k, v in fabric.items():
    if v >= 2:
        count += 1
print(count)

# recheck each claim

for l in claims:
    r, c, w, h, id = l
    intact = True

    for r in range(l[0], l[0] + l[3]):
        for c in range(l[1], l[1] + l[2]):
            # check
            intact = intact and fabric[(r, c)] == 1
            if not intact:
                break
        if not intact:
            break
    else:
        print(f"intact {id}")
