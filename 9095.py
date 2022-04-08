from sys import stdin
input = stdin.readline

n = int(input())
temp = []
cnt = 0

def dsf(T, depth):
    global cnt
    if sum(temp) == T:
        cnt += 1
        return
    if sum(temp) > T: return
    if depth == 0: return
    
    for i in range(1, 4):
        temp.append(i)
        dsf(T, depth-1)
        temp.pop()

for _ in range(n):
    T = int(input())
    dsf(T, T)
    print(cnt)
    cnt = 0