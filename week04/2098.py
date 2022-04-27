from sys import stdin
input = stdin.readline
INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[None] * (1 << n) for _ in range(n)]

def tsp(x, visited):
    if visited == (1<<n) - 1:
        return arr[x][0] or INF
    
    if dp[x][visited]:
        return dp[x][visited]
    
    dp[x][visited] = INF
    
    for i in range(1, n):
        if visited & (1 << i) or arr[x][i] == 0: continue
        dp[x][visited] = min(dp[x][visited], tsp(i, visited | (1<<i)) + arr[x][i])
    
    return dp[x][visited]

print(tsp(0, 1))