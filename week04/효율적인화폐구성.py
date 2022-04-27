from sys import stdin
input = stdin.readline
INF = 10001

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))

dp = [INF] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(arr[i], M + 1):
        if dp[j - arr[i]] != INF:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

print(-1) if dp[M] == INF else print(dp[M])