from dateutil import parser
import sys
from collections import defaultdict


def parse_input(line):
    later = line.partition(" ")[2].partition(" ")[2]
    time = parser.parse(line.split("]")[0][1:])
    return (time, later)


lines = []

for l in sys.stdin:
    lines.append(parse_input(l.strip()))

lines.sort()
guard_id = -1
guard_sleep_count = defaultdict(int)
guard_sleep_track = defaultdict(lambda: [0 for _ in range(60)])

for l in lines:
    time, desc = l
    if "Guard" in desc:
        guard_id = int(desc.split()[1][1:])

    if "wakes" in desc:
        guard_sleep_count[guard_id] += time.minute - pref_time.minute
        for m in range(pref_time.minute, time.minute):
            guard_sleep_track[guard_id][m] += 1

    pref_time = time

max_id = -1
max_count = -1

for k, v in guard_sleep_count.items():
    if v > max_count:
        max_id = k
        max_count = v

print("max id {} {}m".format(max_id, max_count))

max_minute = -1
max_count = 0

for k, v in enumerate(guard_sleep_track[max_id]):
    if v > max_count:
        max_count = v
        max_minute = k

print("at minute", max_minute)

print("strat 2")

max_id = -1
max_minute = -1
max_count = -1

for k, v in guard_sleep_track.items():
    for time, count in enumerate(v):
        if count > max_count:
            max_id = k
            max_minute = time
            max_count = count

print("id {} min {} count {}".format(max_id, max_minute, max_count))
