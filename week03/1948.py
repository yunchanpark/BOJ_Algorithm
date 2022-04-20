from collections import deque
from sys import stdin
input = stdin.readline
INF = float('inf')  # 무한

# 도시 개수
n = int(input())
# 도로 개수
m = int(input())
# 출발 도시 -> 도착 도시, 비용 그래프
graph = [[] for _ in range(n + 1)]
# 도착 도시 -> 출발 도시, 비용 그래프
graph_reverse = [[] for _ in range(n + 1)]
# 그래프 초기화
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph_reverse[end].append((cost, start))
# 도시 출발, 도시 도착
city_start, city_end = map(int, input().split())
# 초기에 도로를 지나기 위한 최소 비용 무한으로 초기화
distance = [-INF] * (n + 1)
# 중복 제거 배열
result = set()

def dijkstra(start):
    queue = deque()
    queue.append((0, start))
    distance[start] = 0

    while queue:
        dist, now = queue.popleft()
        if distance[now] > dist:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost > distance[i[1]]:
                distance[i[1]] = cost
                queue.append((cost, i[1]))


def bfs(end):
    queue = deque()
    queue.append([end, 0])
    # nodes_inv는 그래프의 head와 tail을 거꾸로 만든 그래프
    while queue:
        cur_node, cur_cost = queue.popleft()
        for post_cost, post_node in graph_reverse[cur_node]:
            if distance[cur_node] == post_cost + distance[post_node] and tuple((post_node, cur_node)) not in result:
                # post_cost를 사용한 루트가 최장 거리일 때에만 추적한다. 이때 중복 간선을 체크하기 위해 set으로 확인.
                result.add(tuple((post_node, cur_node)))
                queue.append([post_node, cur_cost+post_cost])


dijkstra(city_start)
bfs(city_end)
print(distance[city_end])
print(len(result))
