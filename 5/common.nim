proc react*(polymer: string): int =
  var stack = newSeq[char](0)
  stack.add(polymer[0])

  for c in polymer[1..<polymer.len]:
    if (ord(stack[^1]) xor ord(c)) == 32:
      discard stack.pop()
    else:
      stack.add(c)

  result = stack.len
