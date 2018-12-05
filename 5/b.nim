from common import react
from sequtils import filter
from strutils import toUpperAscii, join

proc filter_polymer(polymer: string, c: char): string =
  var f = proc (x: char): bool = (x != c) and (x != toUpperAscii(c))
  var r = filter(polymer, f) 
  result = cast[string](r)

var line = readLine(stdin)
var max_len = line.len + 1

for i in 'a'..'z':
  var filtered = filter_polymer(line, i)
  var reacted = react(filtered)
  if reacted.len < max_len:
    max_len = reacted.len
    echo i & ' ' & $(max_len)