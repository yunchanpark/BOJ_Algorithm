input = __import__('sys').stdin.readline
N = int(input())
D_arr = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
max_v = -1e9
min_v = 1e9


def dfs(cnt, value, plus, minus, multi, div):
    global max_v
    global min_v

    if cnt == N:
        max_v = max(max_v, value)
        min_v = min(min_v, value)
    if plus > 0:
        dfs(cnt+1, value + D_arr[cnt], plus-1, minus, multi, div)
    if minus > 0:
        dfs(cnt+1, value - D_arr[cnt], plus, minus-1, multi, div)
    if multi > 0:
        dfs(cnt+1, value * D_arr[cnt], plus, minus, multi-1, div)
    if div > 0:
        dfs(cnt+1, -((-value) // (D_arr[cnt])) if value <
            0 else value // D_arr[cnt], plus, minus, multi, div-1)


dfs(1, D_arr[0], plus, minus, multi, div)
print(max_v)
print(min_v)
