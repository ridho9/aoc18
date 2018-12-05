from strutils import toUpperAscii, join

iterator filter_polymer(polymer: seq[char], c: char): char =
  var cu = toUpperAscii(c)
  for x in polymer:
    if (x != c) and (x != cu):
      yield x

proc react_f(polymer: seq[char], c: char): int =
  var stack = newSeq[char](0)

  for x in filter_polymer(polymer, c):
    if stack.len == 0:
      stack.add(x)
      continue
    
    if (stack[^1].ord xor x.ord) == 32:
      discard stack.pop()
    else:
      stack.add(x)

  result = stack.len

var line = cast[seq[char]](readLine(stdin))
shallow(line)

var max_len = line.len + 1
# part 2
for i in 'a'..'z':
  var count = line.react_f(i)
  if count < max_len:
    max_len = count
    echo i, ' ', max_len