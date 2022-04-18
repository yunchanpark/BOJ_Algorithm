from collections import deque
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
d = ((0,1), (1,0), (0,-1), (-1,0))

queue = deque([[0,0]])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    
    if x == N - 1 and y == M - 1:
        print(visited[x][y])
        break
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])