from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N-1,-1,-1):
    if coins[i] > K: continue
    cnt += K//coins[i]
    K %= coins[i]
print(cnt)