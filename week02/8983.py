from sys import stdin
input = stdin.readline

M, N, L = map(int, input().split()) # 사대 수, 동물 수, 사정거리
M_x = sorted(list(map(int, input().split()))) # 사대 위치 x좌표
A_x_y = [list(map(int, input().split())) for _ in range(N)] # 동물 위치 [x,y] 좌표

cnt = 0
for i in A_x_y:
    start, end= 0, M - 1
    while start <= end:
        mid = (start + end) // 2
        if abs(i[0] - M_x[mid]) + i[1] <= L:
            cnt += 1
            break
        if i[0] > M_x[mid]:
            start = mid + 1
        else:
            end = mid - 1
print(cnt)

# cnt = 0
# for i in A_x_y:
#     if i[1] > L: continue
#     temp = abs(i[1] - L)
#     start = i[0] - temp 
#     end = i[0] + temp
#     for j in M_x:
#         if start <= j <= end:
#             cnt += 1
#             break
# print(cnt)