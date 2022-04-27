from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        if i  <= 2:
            dp[i] = 1
        else:
            dp[i] = dp[i-3] + dp[i-2]
    print(dp[N-1])