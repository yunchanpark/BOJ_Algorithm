from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
input = stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    for i in tree[start]:
        if not parents[i]:
            parents[i] = start
            dfs(i)

dfs(1)
for i in range(2, N + 1):
    print(parents[i])
