from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
queue = deque([i+1 for i in range(n)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.pop())