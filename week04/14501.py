from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    if i + arr[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i + 1])
print(dp[0])