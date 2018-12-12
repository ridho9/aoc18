from collections import defaultdict
import sys

init_state = input().split()[2].replace("#", "1").replace(".", "0")
# print(len(init_state))
input()

pots = set()
for k, v in enumerate(init_state):
    if v == "1":
        pots.add(k)

spread = defaultdict(int)
for l in sys.stdin:
    l = l.strip().replace("#", "1").replace(".", "0")
    left, _, right = l.partition(" => ")
    right = int(right)
    left = int(left, 2)
    spread[left] = right

# for k, v in spread.items():
#     print("{:05b}".format(k), k, v)


def pots_get(pots, idx):
    if idx in pots:
        return 1
    else:
        return 0


def pots_render(pots, start, end):
    res = ''
    for i in range(start, end):
        if pots_get(pots, i) == 1:
            res += "#"
        else:
            res += "."
    return res


max_gen = 200

gen = 0
# print(pots_render(pots, -3, 36))

while gen < max_gen:
    gen += 1
    # print("gen", gen)
    low = min(pots) - 2
    high = max(pots) + 2
    new_pot = set()
    for idx in range(low, high + 1):
        state = 0
        # print("idx", idx)
        for i in range(idx - 2, idx + 3):
            state <<= 1
            state += pots_get(pots, i)
            # print("i", i, state, "{:05b}".format(state))
        # print(" result:", idx, state, "\t{:05b}".format(state), spread[state])
        if spread[state] == 1:
            new_pot.add(idx)
    pots = new_pot
    # print(len(pots), pots)
    # print("{:05} {:05}".format(gen, len(pots)), pots_render(pots, 50, 300))
    print("{:06} {:05}".format(gen, len(pots)))

    total = 0
    for i in pots:
        total += i
    print(total, len(pots))
    # print(total, sorted(pots))
