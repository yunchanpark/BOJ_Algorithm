from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

temp = []

def dsf(m, k, idx):
    if m == 0:
        print(*temp)
        return
    
    for i in range(1, n + 1):
        if idx >= i: continue
        temp.append(i)
        dsf(m - 1, k + 1, i)
        temp.pop()

dsf(m, 0, 0)