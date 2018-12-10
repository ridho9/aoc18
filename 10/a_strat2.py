import sys
import re
import matplotlib.pyplot as plt

data = [tuple(map(int, re.findall(r"-?\d+", x))) for x in sys.stdin]
xs = [a for a, b, c, d in data]
ys = [b for a, b, c, d in data]
speed = [(c, d) for a, b, c, d in data]


def show(data):
    plt.scatter(xs, ys)
    plt.show()


c = 0

while True:
    for i in range(len(data)):
        xs[i] += speed[i][0]
        ys[i] += speed[i][1]
    c += 1
    if max(ys) - min(ys) <= 10:
        show(data)
