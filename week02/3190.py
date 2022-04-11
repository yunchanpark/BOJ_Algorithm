from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())  # 보드 크기
k = int(input())  # 사과 개수
broad = [[0]*n for _ in range(n)]  # 보드 배열

# 보드에 사과 위치 표시
for _ in range(k):
    x, y = map(int, input().split())
    broad[x-1][y-1] = 1

# 시간초, 방향 배열
cnt = int(input())
td_arr = {}
for _ in range(cnt):
    a, b = input().split()
    td_arr[int(a)] = b

# 오른쪽으로 갈때는 x좌표만 + 1
# 왼쪽으로 갈때는 x좌표만 - 1
# 위로 갈때는 y좌표만 -1
# 아래로 갈때는 y좌표만 +1
d_x = deque([0, 1, 0, -1])  # x좌표 오른쪽, 아래, 왼쪽, 위 순
d_y = deque([1, 0, -1, 0])  # y좌표 오른쪽, 아래, 왼쪽, 위 순

# 뱀의 꼬리부터 머리까지 위치가 담긴 큐
# 시작 위치는 [0,0]이기 때문에 미리 담아줌
snack_queue = deque()
snack_queue.append([0, 0])

seconds = d_idx = x = y = 0  # 시간, 방향 인덱스, 뱀의 x 좌표, 뱀의 y 좌표
# 방향 전환


def change(d):
    if d == 'L':
        d_x.rotate(1)
        d_y.rotate(-1)
    else:
        d_x.rotate(-1)
        d_y.rotate(1)


# 뱀 이동
while True:
    seconds += 1
    x += d_x[0]
    y += d_y[0]

    if 0 <= x < n and 0 <= y < n and [x, y] not in snack_queue:
        snack_queue.append([x, y])
        # 사과를 먹었을 때
        if broad[x][y] == 1:
            broad[x][y] = 0
        else:
            snack_queue.popleft()
        if seconds in td_arr.keys():
            change(td_arr[seconds])
    else:
        break
print(seconds)
