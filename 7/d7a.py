import sys
from collections import defaultdict

graph = defaultdict(lambda: [])
before = defaultdict(lambda: [])
nodes = set()

for l in sys.stdin:
    l = l.split()
    h, t = l[1], l[7]
    graph[h].append(t)
    before[t].append(h)
    nodes.add(h)
    nodes.add(t)

start = '0'
for node in nodes:
    if before.get(node) == None:
        graph['0'].append(node)
        before[node].append('0')

for k, v in graph.items():
    graph[k] = sorted(v)
for k, v in before.items():
    before[k] = sorted(v)

print(graph['0'])
print(graph)

# print(edges)
# print(graph)
# print(before)
# print(nodes)
# print(start)

queue = ['0']
visited = defaultdict(lambda: False)

res = ''

while len(queue) != 0:
    head = queue[0]
    queue = queue[1:]
    res += head
    print(head)
    visited[head] = True
    for next in graph[head]:
        print('n:', next, end='')
        # check before
        allowed = True
        for pre in before[next]:
            allowed = allowed and visited[pre]
        print(allowed)

        if (not visited[next]) and allowed:
            queue.append(next)
    queue.sort()
    print('[{}]'.format(queue))

print('')

print(res)
print(len(res))
