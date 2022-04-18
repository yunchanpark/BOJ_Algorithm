input = __import__('sys').stdin.readline

# 컴퓨터의 수
N = int(input())
# 간선의 수
E = int(input())
# 컴퓨터 연결을 일단 자기 자신으로 지정
parents = [i for i in range(N + 1)]

# 부모 컴퓨터 찾기
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# 컴퓨터 연결
def union(start, end):
    start = find(start)
    end = find(end)
    if start > end:
        parents[start] = end
    else:
        parents[end] = start

for _ in range(E):
    start, end = map(int, input().split())
    union(start, end)

for i in range(1, N + 1):
    find(i)

print(parents.count(1) - 1)

# input = __import__('sys').stdin.readline

# # 컴퓨터 개수
# N = int(input())
# # 간선 개수
# E = int(input())
# # 컴퓨터 연결
# com_list = [[] for _ in range(N + 1)]
# # 방문 처리
# visited = [False] * (N + 1)
# def dfs(n):
#     visited[n] = True
#     for i in com_list[n]:
#         if not visited[i]:
#             dfs(i)

# for i in range(E):
#     a, b = map(int, input().split())
#     com_list[a].append(b)
#     com_list[b].append(a)
    
# dfs(1)
# print(visited.count(1) - 1)