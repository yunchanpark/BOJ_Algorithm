from sys import stdin
from heapq import heappop, heappush

N = int(input())
node = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
result = [0] * (N + 1)

for x in range(1, N + 1):
    num = list(map(int, '0' + input().rstrip()))
    for y, data in enumerate(num):
        if data == 1:
            node[y].append(x)
            degree[x] += 1

def topology():
    heap = []
    n = N
    
    for i in range(1, N + 1):
        if degree[i] == 0:
            heappush(heap, -i)
    
    while heap:
        now = -heappop(heap)
        result[now] = n
        
        for i in node[now]:
            degree[i] -= 1
            if degree[i] == 0:
                heappush(heap, -i)
        n -= 1
    return result

topology()
if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])