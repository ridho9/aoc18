import sys
from itertools import cycle

track = []
for line in sys.stdin:
    track.append(list(line.strip('\n')))

height = len(track)
width = len(track[0])

cars = []
for r in range(height):
    for c in range(width):
        if track[r][c] in [">", "^", "<", "v"]:
            cars.append([r, c, track[r][c], cycle(["l", "s", "r"])])
            if track[r][c] in [">", "<"]:
                track[r][c] = "-"
            else:
                track[r][c] = "|"


def print_track_with_cars():
    global track, cars

    height = len(track)
    width = len(track[0])

    for r in range(height):
        for c in range(width):
            for car in cars:
                a, b, v, _ = car
                if a == r and b == c:
                    print(v, end='')
                    break
            else:
                print(track[r][c], end='')
        print('')


# print_track_with_cars()

tick = 0

crashed = False
while not crashed:
    # if tick > 20:
    #     break
    # print(tick)
    cars.sort()

    for idx, car in enumerate(cars):
        r, c, v, turn = car
        t = track[r][c]

        if t == "+":
            intersect = next(turn)
            if v == ">":
                if intersect == "l":
                    r -= 1
                    v = "^"
                elif intersect == "s":
                    c += 1
                elif intersect == "r":
                    r += 1
                    v = "v"
            elif v == "^":
                if intersect == "l":
                    c -= 1
                    v = "<"
                elif intersect == "s":
                    r -= 1
                elif intersect == "r":
                    c += 1
                    v = ">"
            elif v == "<":
                if intersect == "l":
                    r += 1
                    v = "v"
                elif intersect == "s":
                    c -= 1
                elif intersect == "r":
                    r -= 1
                    v = "^"
            elif v == "v":
                if intersect == "l":
                    c += 1
                    v = ">"
                elif intersect == "s":
                    r += 1
                elif intersect == "r":
                    c -= 1
                    v = "<"
        else:
            if v == ">":
                if t == "-":
                    c += 1
                elif t == "\\":
                    r += 1
                    v = "v"
                elif t == "/":
                    r -= 1
                    v = "^"
            elif v == "^":
                if t == "|":
                    r -= 1
                elif t == "\\":
                    c -= 1
                    v = "<"
                elif t == "/":
                    c += 1
                    v = ">"
            elif v == "<":
                if t == "-":
                    c -= 1
                elif t == "\\":
                    r -= 1
                    v = "^"
                elif t == "/":
                    r += 1
                    v = "v"
            elif v == "v":
                if t == "|":
                    r += 1
                elif t == "\\":
                    c += 1
                    v = ">"
                elif t == "/":
                    c -= 1
                    v = "<"

        cars[idx] = [r, c, v, turn]
        coords = set()
        for ic, c in enumerate(cars):
            toin = (c[0], c[1])
            if toin in coords:
                print("{},{}".format(toin[1], toin[0]))
                crashed = True
            else:
                coords.add(toin)

    tick += 1
