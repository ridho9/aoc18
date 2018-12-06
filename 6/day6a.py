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

field = defaultdict(int)
near = {}


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for x in range(xs[0] - x_span // 2, xs[-1] + x_span // 2):
    for y in range(ys[0] - y_span // 2, ys[-1] + y_span // 2):
        dist = {}
        for i, p in enumerate(points):
            dist[i] = man_dist([x, y], p)
        dist = sorted(dist.items(), key=lambda x: x[1])
        if dist[0][1] == dist[1][1]:
            near[(x, y)] = -1
        else:
            near[(x, y)] = dist[0][0]

on_border = set()

for x in range(xs[0] - x_span // 2, xs[-1] + x_span // 2):
    for y in range(ys[0] - y_span // 2, ys[-1] + y_span // 2):
        if (x == xs[0] - x_span // 2) or (x == xs[-1] + x_span // 2 - 1):
            on_border.add(near[(x, y)])
        if (y == ys[0] - y_span // 2) or (y == ys[-1] + y_span // 2 - 1):
            on_border.add(near[(x, y)])

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

count = defaultdict(int)

for a, b in near.items():
    count[b] += 1

count = sorted(count.items(), key=lambda x: x[1])
print(len(count))
print(count)
print(on_border)

count = list(filter(lambda x: x[0] not in on_border, count))
print(len(count))
print(count)
