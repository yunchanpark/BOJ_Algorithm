n = int(input())

min_size = 10000001
arr = [list(map(int, input().split())) for _ in range(n)]

visitedX = [0]*n
visitedY = [0]*n

def dsf(idx, k, t, value):
    global min_size
    if k == n - 1:
        if arr[idx][t] != 0:
            min_size = min(min_size, value + arr[idx][t])
        return
    
    if value > min_size:
        return
    
    for i in range(n):
        if arr[idx][i] != 0 and visitedX[i] == 0 and visitedY[i] == 0:
            visitedX[idx] = 1
            visitedY[i] = 1
            dsf(i, k + 1, t, value + arr[idx][i])
            visitedX[idx] = 0
            visitedY[i] = 0
for i in range(n):
    dsf(i, 0, i, 0)
print(min_size)