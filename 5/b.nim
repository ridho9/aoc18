from common import react
from sequtils import filter
from strutils import toUpperAscii, join

proc filter_polymer(polymer: string, c: char): string =
  var cu = toUpperAscii(c)
  var r = filter(polymer) do (x: char) -> bool: (x != c) and (x != cu)
  result = cast[string](r)

var line = readLine(stdin)
var max_len = line.len + 1

for i in 'a'..'z':
  var filtered = filter_polymer(line, i)
  var reacted = react(filtered)
  if reacted < max_len:
    max_len = reacted
    echo i & ' ' & $(max_len)