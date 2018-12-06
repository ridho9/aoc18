import sys
from collections import defaultdict

points = []
xs = []
ys = []

for l in sys.stdin:
    p = [int(x) for x in l.split(',')]
    xs.append(p[0])
    ys.append(p[1])
    points.append(p)

xs.sort()
ys.sort()

x_span = xs[-1] - xs[0]
y_span = ys[-1] - ys[0]

count = defaultdict(int)


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for x in range(xs[0] - x_span // 2, xs[-1] + x_span // 2):
    for y in range(ys[0] - y_span // 2, ys[-1] + y_span // 2):
        for i, p in enumerate(points):
            count[(x, y)] += man_dist([x, y], p)

res = 0

for p, c in count.items():
    if c < 10000:
        res += 1

print(res)

# for x in range(xs[0] - x_span // 2, xs[-1] + x_span // 2):
#     for y in range(ys[0] - y_span // 2, ys[-1] + y_span // 2):
#         if [x, y] in points:
#             idx = points.index([x, y])
#             print(chr(idx + ord('A')), end='')
#         elif near[(x, y)] == -1:
#             print('.', end='')
#         else:
#             print(near[(x, y)], end='')
#     print()
