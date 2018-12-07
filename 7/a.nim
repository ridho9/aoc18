from algorithm import SortOrder, sort

var
  l, res: string
  next, before: array['A'..'Z', seq[char]]
  queue = newSeq[char](0)
  visited: set[char]
  h, t: char

while stdin.readLine(l):
  h = l[5]
  t = l[36]
  next[h].add(t)
  before[t].add(h)

for k, v in next:
  if (v.len != 0) and (before[k].len == 0):
    queue.add(k)
  
while queue.len > 0:
  queue.sort(SortOrder.Descending)
  h = queue.pop()
  res &= h
  visited.incl(h)
  for t in next[h]:
    var allowed = true
    for preq in before[t]:
      allowed = allowed and (preq in visited)
    if allowed:
      queue.add(t)
  
echo res