from collections import deque
input = __import__('sys').stdin.readline

# N: 정점의 개수, M: 간선의 개수, V: 시작할 정점의 번호
N, M, V = map(int, input().split())
# 2차원 배열로 그래프 초기화
graph = [[0] * (N + 1) for _ in range(N + 1)]

# 노드 연결
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = 1

# 깊이 우선 탐색
# start: 시작할 정점의 번호
# temp: 방문처리
def dfs(start, temp=[]):
    temp.append(start)
    print(start, end=' ')
    for end in range(len(graph[start])):
        if graph[start][end] == 1 and (end not in temp):
            dfs(end, temp)

# 너비 우선 탐색
def bfs(start):
    temp = [start]
    # 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(N)이다.
    # deque는 시간복잡도가 O(1)이다
    queue = deque(temp)
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for end in range(len(graph[start])):
            if graph[v][end] == 1 and (end not in temp):
                temp.append(end)
                queue.append(end)
dfs(V)
print()
bfs(V)