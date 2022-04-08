from sys import stdin
input = stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
temp = []
cnt = 0

def dsf(depth, idx):
    global cnt
    global s
    global n
    if sum(temp) == s and depth != 0:
        cnt += 1
    if depth == n: 
        return
    
    for i in range(n):
        if idx < i:
            temp.append(arr[i])
            dsf(depth + 1, i)
            temp.pop()
dsf(0, -1)
print(cnt)