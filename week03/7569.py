from collections import deque
from sys import stdin
input = stdin.readline

# row: 행, col: 열, hight: 높이
col, row, hight = map(int, input().split())
# 3차원 배열
arr = [[[0] * col for _ in range(row)] for _ in range(hight)]
# 상, 하, 좌, 우, 위, 아래
direction = ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0))
# 익은 토마토를 담는 큐
queue = deque()
# 일수
day = 0

# 3차원 배열 값 초기화
# 토마토가 있는 곳은 queue에 담음
for z in range(hight):
    for x in range(row):
        temp = list(map(int, input().split()))
        for y, data in enumerate(temp):
            arr[z][x][y] = data
            if data == 1:
                queue.append((z, x, y, 0))

while queue:
    z, x, y, cnt = queue.popleft()
    for dz, dx, dy in direction:
        new_z = z + dz
        new_x = x + dx
        new_y = y + dy
        # 행과 열과 높이를 넘지 않을 때
        if 0 <= new_z < hight and 0 <= new_x < row and 0 <= new_y < col:
            if arr[new_z][new_x][new_y] == 0:
                arr[new_z][new_x][new_y] = 1
                day = cnt + 1
                queue.append((new_z, new_x, new_y, cnt + 1))

for z in range(hight):
    for x in range(row):
        if arr[z][x].count(0):
            day = -1
            break

print(day)
