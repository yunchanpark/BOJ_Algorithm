from sys import stdin
input = stdin.readline

row, col = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(row)])
dp = [0] * (col + 1)

for w, v in arr:
    for i in range(col, -1, -1):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i-w] + v)
        else: 
            break
        
print(dp)