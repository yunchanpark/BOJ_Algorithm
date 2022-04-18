from sys import setrecursionlimit, stdin 
setrecursionlimit(10**9)
input = stdin.readline

def dfs(start, cnt):
    visited[start] = True
    for i in graph[start]:
        if A[i] == 1:
            cnt += 1
        elif not visited[i] and A[i] == 0:
            cnt = dfs(i, cnt)
    return cnt

N = int(input())
A = list(map(int, list("0"+input().strip())))

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = 0
sum = 0

for _ in range(N - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    if A[start] == 1 and A[end] == 1:
        ans += 2


for i in range(1, N + 1):
    if not visited[i] and A[i] == 0:
        x = dfs(i, 0)
        sum += x*(x-1)

print(sum + ans)