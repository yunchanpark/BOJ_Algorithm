from sys import stdin
from collections import deque
input = stdin.readline

# N: 행, M: 열
N, M = map(int, input().split())
# 맵 배열
arr = [list(map(int, input().rstrip())) for _ in range(N)]
# 방문체크
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
# 이동할 큐
queue = deque()
# 방향
direction = ((-1,0), (1,0), (0,-1), (0,1))

def bfs():
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        wall, x, y = queue.popleft()
        if x == N - 1 and y == M -1:
            print(visited[x][y][wall])
            return
        for dx, dy in direction:
            new_x = x + dx
            new_y = y + dy
            if 0 > new_x or new_x >= N or 0 > new_y or new_y >= M or visited[new_x][new_y][wall] != 0:
                continue
            if arr[new_x][new_y] == 0:
                queue.append((wall, new_x, new_y))
                visited[new_x][new_y][wall] = visited[x][y][wall] + 1
            if arr[new_x][new_y] == 1 and wall == 0:
                queue.append((1, new_x, new_y))
                visited[new_x][new_y][1] = visited[x][y][wall] + 1
    print(-1)
bfs()