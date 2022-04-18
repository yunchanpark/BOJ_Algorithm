from collections import deque
from sys import stdin
input = stdin.readline

# 시작 위치 담을 큐
start_queue = deque()
# 끝 위치 담을 큐
end_queue = deque()
# 물 위치 담을 큐
water_queue = deque()
# 상하좌우
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
# row: 행, col: 열
row, col = map(int, input().split())
# 물 상태 배열
water_arr = [[-1] * col for _ in range(row)]
# 이동 상태 배열
move_arr = [[-1] * col for _ in range(row)]
# 현재 굴 상태 배열
arr = [[0] * col for _ in range(row)]
# 현재 굴 상태 초기화, 물이 있는 위치, 시작점, 끝점 각각의 큐에 담기
for x in range(row):
    temp = list(input().rstrip())
    for y, data in enumerate(temp):
        arr[x][y] = data
        if data == 'D':
            end_queue.append((x, y))
        if data == 'S':
            start_queue.append((x, y))
            move_arr[x][y] = 0
        elif data == '*':
            water_queue.append((x, y))
            water_arr[x][y] = 0

# 물이 차는 경로 표시
while water_queue:
    x, y = water_queue.popleft()
    for dx, dy in direction:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < row and 0 <= new_y < col and \
            arr[new_x][new_y] == '.' and water_arr[new_x][new_y] == -1:
            water_arr[new_x][new_y] = water_arr[x][y] + 1
            water_queue.append((new_x, new_y))

# 이동 경로 표시
while start_queue:
    x, y = start_queue.popleft()
    for dx, dy in direction:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < row and 0 <= new_y < col and arr[new_x][new_y] in '.D' and move_arr[new_x][new_y] == -1 and\
                (move_arr[x][y] + 1 < water_arr[new_x][new_y] or water_arr[new_x][new_y] == -1):
            move_arr[new_x][new_y] = move_arr[x][y] + 1
            start_queue.append((new_x, new_y))

x, y = end_queue.popleft()
result = move_arr[x][y]
if result == -1:
    result ='KAKTUS'
print(result)