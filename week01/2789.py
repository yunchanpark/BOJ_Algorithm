from sys import stdin, maxsize
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
select = [False]*n
ans = maxsize

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = True
        dfs(i + 1, cnt + 1)
        select[i] = False

dfs(0, 0)
print(ans)