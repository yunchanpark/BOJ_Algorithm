import sys
from itertools import combinations
input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]

a = combinations(arr, 7)
for i in a:
    if sum(i) == 100:
        i = sorted(i)
        for j in i:
            print(j)
        break