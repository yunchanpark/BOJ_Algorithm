from sys import stdin
from tabnanny import check
input = stdin.readline

N = int(input())
stack = []
result = []
cnt = 1
check = True

for _ in range(N):
    k = int(input())
    
    while cnt <= k:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    
    if stack[-1] == k:
        stack.pop()
        result.append('-')
    else:
        check = False
        print('NO')
        break
if check:
    while stack:
        stack.pop()
        result.append('-')
    print(*result, sep='\n')
