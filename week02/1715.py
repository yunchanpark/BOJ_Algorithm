from sys import stdin
import heapq

input = stdin.readline
n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))
result = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    temp = a + b
    heapq.heappush(arr, temp)
    result += temp
print(result)