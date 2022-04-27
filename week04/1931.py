from sys import stdin
input = stdin.readline

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))
cnt = 1
now = arr[0][1]

for i in range(1, N):
    if now <= arr[i][0]:
        cnt += 1
        now = arr[i][1]
print(cnt)