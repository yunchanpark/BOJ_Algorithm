from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N +1)]
indegree = [0] * (N + 1)
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1

def topology():
    result = []
    queue = deque()
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(*result)
topology()