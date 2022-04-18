input = __import__('sys').stdin.readline

# N: 정점의 개수, M: 간선의 개수
N, M = map(int, input().split())
# 부모 테이블 초기화
parent = [i for i in range(N + 1)]

# 특정 원소가 속한 집합을 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(start, end):
    start = find(start)
    end = find(end)
    if start != end:
        parent[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    if find(start) != find(end):
        union(start, end)

for i in range(1, N+1):
    find(i)

s = set(filter(lambda x: x > 0, parent))
print(len(s))