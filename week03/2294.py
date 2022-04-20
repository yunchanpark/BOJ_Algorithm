from sys import stdin
from collections import deque
input = stdin.readline

# n: 동전 종류 개수, k: 원하는 값
n, k = map(int, input().split())
coin_arr = set([int(input()) for _ in range(n)])
visited = [0 for _ in range(k + 1)]
queue = deque()

for coin in coin_arr:
    if coin <= k:
        queue.append([coin, 1])
        visited[coin] = 1

def bfs():
    while queue:
        value, cnt = queue.popleft()
        if value == k:
            return cnt

        for coin in coin_arr:
            temp = value + coin
            if temp > k:
                continue
            if visited[temp] == 0:
                visited[temp] = 1
                queue.append([temp, cnt + 1])
    return -1
print(bfs())
