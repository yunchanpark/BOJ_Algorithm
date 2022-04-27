from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    DP = [0] * (M + 1)
    DP[0] = 1
    for i in arr:
        for j in range(1, M + 1):
            if j - i >= 0:
                DP[j] += DP[j - i]
    print(DP[M])