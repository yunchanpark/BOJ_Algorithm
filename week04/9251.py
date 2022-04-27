from sys import stdin
input = stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
row, col = len(str1), len(str2)

dp = [[0] * (col + 1) for _ in range(row + 1)]
for i in range(1, row+1):
    for j in range(1, col+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[row][col])