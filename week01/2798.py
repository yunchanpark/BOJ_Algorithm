import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

a = sorted(arr, reverse=True)
b = []
temp = permutations(a, 3)
for i in temp:
    if sum(i) <= m:
        b.append(sum(i))

print(max(b))