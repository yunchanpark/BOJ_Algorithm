from sys import stdin
import heapq

input = stdin.readline
n = int(input())

left_arr = []
right_arr = []

for _ in range(n):
    num = int(input())
    
    if len(left_arr) == len(right_arr):
        heapq.heappush(left_arr, -num)
    else:
        heapq.heappush(right_arr, num)
    if right_arr and -left_arr[0] > right_arr[0]:
        max = heapq.heappop(left_arr)
        min = heapq.heappop(right_arr)
        heapq.heappush(left_arr, -min)
        heapq.heappush(right_arr, -max)
    print(-left_arr[0])