from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int, input().split())) for _ in range(N))
    now = arr[0][1]
    cnt = 1
    for first, second in arr:
        if now > second:
            cnt += 1 
            now = second
    print(cnt)