import sys
input = sys.stdin.readline
n = int(input())
c = [0] * 10001

for _ in range(n):
    a = int(input())
    c[a] += 1

for i in range(10001):
    if c[i] != 0:
        for _ in range(c[i]):
            print(i)