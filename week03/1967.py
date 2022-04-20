from sys import stdin
from collections import deque
input = stdin.readline
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
    graph[end].append([start, cost])

def bfs(start):
    queue = deque()
    queue.append(start)
    temp = [-1 for _ in range(n + 1)]
    temp[start] = 0
    while queue:
        x = queue.popleft()
        for node, cost in graph[x]:
            if temp[node] == -1:
                temp[node] = temp[x] + cost
                queue.append(node)
    return temp.index(max(temp)), max(temp)

node, dist = bfs(1)
node, dist = bfs(node)
print(dist)