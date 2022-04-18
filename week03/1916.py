import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9) # 무한을 의미하는 10억을 설정

# 도시 개수
N = int(input())
# 버스 개수
M = int(input())
# 도로 간선
graph = [[] for _ in range(N + 1)]
# 도로 간선 값 초기화
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
# 출발지, 도착지
start, end = map(int, input().split())
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
print(distance[end])