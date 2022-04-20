from sys import stdin
input = stdin.readline

# N: 구슬 개수, M: 저울에 올려 본 쌍의 개수
N, M = map(int, input().split())
# 큰 값 담기
max_graph = [[] for _ in range(N + 1)]
# 작은 값 담기
min_graph = [[] for _ in range(N + 1)]
# 결과
result = 0
for _ in range(M):
    start, end = map(int, input().split())
    max_graph[end].append(start)
    min_graph[start].append(end)

def dfs(start, cnt, arr, visited):
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            cnt = dfs(i, cnt + 1, arr, visited)
    return cnt

for i in range(1, N + 1):
    cnt = 0
    if dfs(i, cnt, max_graph, [False] * (N + 1)) >= (N + 1) // 2:
        result += 1
    if dfs(i, cnt, min_graph, [False] * (N + 1)) >= (N + 1) // 2:
        result += 1
        
print(result)