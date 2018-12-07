from algorithm import SortOrder, sort

var
  l, res: string
  next, before: array['A'..'Z', seq[char]]
  jobs = newSeq[char](0)
  finished, nodes: set[char]
  h, t: char
  worker = newSeq[char](0)

  time_left: array['A'..'Z', int]
  second = 0

while stdin.readLine(l):
  h = l[5]
  t = l[36]
  next[h].add(t)
  before[t].add(h)
  nodes.incl(h)
  nodes.incl(t)

for k, v in next:
  if (v.len != 0) and (before[k].len == 0):
    jobs.add(k)

for i in 0..<5:
  worker.add('.')

proc assign_job() = 
  jobs.sort(Descending)
  for k, v in worker:
    if v != '.':
      continue
    if jobs.len == 0:
      echo "no job to assign"
      break
    var j = jobs.pop()
    
    time_left[j] = ord(j) - ord('A') + 1 + 60
    worker[k] = j

    echo "Assigned job ", j, " to worker ", k

assign_job()
echo time_left

while finished.card < nodes.card:
  var reassign = false
  echo "second ", second, "\t", worker

  for k, v in worker:
    if v == '.':
      continue
    
    time_left[v] -= 1
    if time_left[v] == 0:
      echo "finished ", v
      reassign = true
      finished.incl(v)
      worker[k] = '.'
      for next in next[v]:
        var allowed = true
        for preq in before[next]:
          allowed = allowed and (preq in finished)
        if allowed:
          jobs.add(next)
          echo "add job ", next
  
  if reassign:
    assign_job()

  second += 1

echo "finished at second ", second