from heapq import heappop, heappush
from sys import stdin
input = stdin.readline
# 방의 수
n = int(input())
# 미로 배열 초기화
arr = [list(map(int, input().rstrip())) for _ in range(n)]
# 상하좌우
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 방문 체크
visited = [[False] * n for _ in range(n)]

def bfs():
    queue = []
    heappush(queue, (0, 0, 0))
    while queue:
        cost, x, y = heappop(queue)
        if x == n - 1 and y == n - 1: return cost
        if visited[x][y]: continue
        visited[x][y] = True
        for dx, dy in direction:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                if arr[new_x][new_y] == 1:
                    heappush(queue, (cost, new_x, new_y))
                else:
                    heappush(queue, (cost + 1, new_x, new_y))
print(bfs())