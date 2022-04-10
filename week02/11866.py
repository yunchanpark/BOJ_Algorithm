from sys import stdin
from collections import deque

input = stdin.readline
n, k = map(int, input().split())

queue = deque([i+1 for i in range(n)])
result = []

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())
    
print(f"<{', '.join(map(str,result))}>")
