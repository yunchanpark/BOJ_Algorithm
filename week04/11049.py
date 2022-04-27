from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        if i == 1:
            dp[j][j+i] = arr[j][0] * arr[j][1] * arr[j+i][1]
        else:
            dp[j][j+i] = 2**32
            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1])
print(dp[0][N-1])  