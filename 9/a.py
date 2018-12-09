from collections import defaultdict
from blist import blist

num_player = 464
max_marble = 70918 * 100

scores = defaultdict(int)

circle = blist([0])
cur_player = 1
last_marble = 1
cur_marble = 0


def cw(l, cur, offset):
    return (cur + offset) % l


def ccw(l, cur, offset):
    return (cur - offset) % l


while last_marble <= max_marble:
    if last_marble % 1000 == 0:
        print(last_marble)

    if last_marble % 23 == 0:
        m = ccw(len(circle), cur_marble, 7)
        scores[cur_player] += last_marble + \
            circle[m]
        del circle[m]
        cur_marble = m
    else:
        cur_marble = cw(len(circle), cur_marble, 2)
        circle.insert(cur_marble, last_marble)

    # print(last_marble, cur_player, circle)

    cur_player += 1
    if cur_player > num_player:
        cur_player = 1
    last_marble += 1

scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(scores[0])
