from sys import stdin
from itertools import permutations
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
b = permutations(arr, n)
c = []
for i in b:
    temp = 0
    for j in range(1, len(i)):
        temp += abs(i[j-1] - i[j])
    c.append(temp)
print(max(c))