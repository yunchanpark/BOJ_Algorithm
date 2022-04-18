input = __import__('sys').stdin.readline

V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
# [n][0]: 시작 정점
# [n][1]: 끝 정점
# [n][2]: 간선의 값
graph = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2]) # 그래프
visited = [i for i in range(V + 1)] # 방문하기 위한 값
answer = 0 # 정답

def find(x):
    if x != visited[x]:
        visited[x] = find(visited[x])
    return visited[x]

# A, B, C: 시작 정점, 끝 정점, 간선의 값
for A, B, C in graph:
    start = find(A)
    end = find(B)
    # 시작 정점 하고 끝 정점이 같지 않으면 연결 되지 않았다는 뜻
    if start != end:
        if start > end:
            visited[start] = end
        else:
            visited[end] = start
        answer += C
print(answer)
# import heapq
# input = __import__('sys').stdin.readline

# V, E = map(int, input().split())
# visited = [False] * (V + 1)
# graph = [[] for _ in range(V + 1)]
# heap = [[0, 1]]
# for _ in range(E):
#     A, B, C = map(int, input().split())
#     graph[A].append([C, B])
#     graph[B].append([C, A])

# answer = 0
# cnt = 0
# while heap:
#     if cnt == V : break
#     C, A = heapq.heappop(heap)
#     if not visited[A]:
#         visited[A] = True
#         answer += C
#         cnt += 1
#         for i in graph[A]:
#             heapq.heappush(heap, i)
# print(answer)