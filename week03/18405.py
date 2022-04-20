from sys import stdin
from collections import deque
input = stdin.readline

# 행과 열
row, col = map(int, input().split())
# 방향
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 큐배열
queue = []
# 방문 체크
visited = [[False] * col for _ in range(row)]
# 바이러스 배열
arr = [[0]*col for _ in range(row)]
# 배열 초기화
for x in range(row):
    temp = list(map(int, input().split()))
    for y, data in enumerate(temp):
        arr[x][y] = data
        if data != 0:
            queue.append([data, x, y])
# 초, x, y 좌표
S, X, Y = map(int, input().split())

cnt = 0
while True:
    if cnt == S: break
    queue = deque(sorted(queue))
    for _ in range(len(queue)):
        data, x, y = queue.popleft()
        visited[x][y] = True
        for dx, dy in direction:
            new_x = x + dx
            new_y = y + dy
            if 0 > new_x or new_x >= row or 0 > new_y or new_y >= row:
                continue
            if not visited[new_x][new_y] and arr[new_x][new_y] == 0:
                arr[new_x][new_y] = data
                queue.append([data, new_x, new_y])
    cnt += 1
    
print(arr[X-1][Y-1])