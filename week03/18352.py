# from sys import stdin
# from collections import deque

# # N: 도시 개수
# # M: 도로 개수
# # K: 거리 정보
# # X: 출발 도시 번호
# N, M, K, X = map(int, input().split())

# graph = [[] for _ in range(N + 1)]
# cost = [0] * (N + 1)
# visited = [False] * (N + 1)
# answer = []

# for _ in range(M):
#     start, end = map(int, input().split())
#     graph[start].append(end)


# def bfs(start):
#     queue = deque([start])
#     cost[start] = 0
#     visited[start] = True
#     while queue:
#         now = queue.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#                 cost[i] = cost[now] + 1
#                 if cost[i] == K:
#                     answer.append(i)
                    
#     if len(answer) == 0:
#         print(-1)
#     else:
#         answer.sort()
#         print(*answer, sep='\n')

# bfs(X)

from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append((end, 1))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
dijkstra(X)

answer = []

for i in range(1, N + 1):
    if distance[i] == K: answer.append(i)

if len(answer) == 0: print(-1)
else: print(*answer, sep='\n')