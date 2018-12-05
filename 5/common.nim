proc react*(polymer: string): string =
  var c1, c2: char
  var polymer = polymer
  var idx = 0
  while idx < polymer.len - 1:
    c1 = polymer[idx]
    c2 = polymer[idx + 1]

    if (ord(c1) xor ord(c2)) == 32:
      polymer = polymer[0 ..< idx] & polymer[idx+2 ..< polymer.len]
      if idx > 0:
        idx -= 1
    else:
      idx += 1
  result = polymer
