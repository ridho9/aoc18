import strscans
import algorithm

type
  Point = tuple[x: int, y: int]

var
  points = newSeq[Point](0)
  xs, ys = newSeq[int](0)
  l: string
  x, y: int

while stdin.readLine(l):
  discard scanf(l, "$i, $i", x, y)
  xs.add(x)
  ys.add(y)
  points.add((x, y))

xs.sort
ys.sort