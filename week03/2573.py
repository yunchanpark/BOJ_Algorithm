from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline

# row: 행, col: 열
row, col = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(row)]  # 빙산 배열
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))                  # 방향, 상하좌우
# 빙산이 2덩어리 이상으로 나누어지는 연도
years = 0
iceberg_cnt = 0                                                 # 빙산 개수
# 연도 마다 물로 변한 빙하
change_water = 0
stack = [[0, 0]]
# 초기 빙산 개수 초기화
for x in range(row):
    for y in range(col):
        if iceberg[x][y] != 0:
            iceberg_cnt += 1


def dfs(x, y, visited, cnt):
    global change_water     # 물로 바뀐 빙하 개수
    visited[x][y] = True    # 현재 좌표 방문 처리
    cnt += 1                # 빙하 개수 카운트
    water = 0               # 주변의 물 개수

    # 현재 좌표에서 상하좌우 살펴봄
    for dx, dy in direction:
        new_x = x + dx
        new_y = y + dy
        # 행과 열을 넘지 않고, 방문하지 않은 곳
        if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y]:
            # 만약 상하좌우 중에 물이 있으면 water를 하나씩 올려줌
            if iceberg[new_x][new_y] == 0:
                water += 1
            # 물이 없으면 빙하이기 때문에 다시 다음 빙하에서 DFS 실행
            else:
                cnt = dfs(new_x, new_y, visited, cnt)
    # 모든 탐색이 끝났으면 현재 빙하에서 water만큼 뺀게 0보다 크면 그냥 빼줌
    # 0보다 작으면 물로 변했다는 의미이기 때문에 change_water를 하나 올려줌
    if iceberg[x][y] - water > 0:
        iceberg[x][y] -= water
    else:
        iceberg[x][y] = 0
        change_water += 1
    return cnt


while True:
    start_x, start_y = stack.pop()
    visited = [[False] * col for _ in range(row)]   # 방문 처리
    cnt = 0
    # 빙산 하나만 찾고 거기서 DFS를 통해 빙산을 개수를 찾음
    for x in range(start_x, row):
        for y in range(start_y, col):
            if iceberg[x][y] != 0:
                cnt = dfs(x, y, visited, cnt)
                stack.append([x, y])
                break
        else:
            continue
        break

    # DFS를 사용하여 찾은 cnt 빙산개수와 기존의 빙하 개수가 같은데
    # cnt가 0이라면 빙산가 다 녹았다는 의미
    # cnt가 0이아니라면 아직 녹을 빙산가 남았기 때문에 years를 1더해줌
    # DFS를 사용하여 찾은 cnt 빙산개수와 기존의 빙하 개수가 다르다면 빙하가 분리되었다는 의미
    if cnt == iceberg_cnt:
        if cnt == 0:
            years = 0
            break
        else:
            years += 1
    else:
        break

    iceberg_cnt -= change_water   # 물로 된 빙산를 원래 빙하 개수에서 뺌
    change_water = 0              # 이번년도에 물로 변했던 빙산 개수를 다시 0으로 초기화
print(years)
