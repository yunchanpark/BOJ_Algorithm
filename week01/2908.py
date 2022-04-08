import sys
a = list(map(str, sys.stdin.readline().split()))
b = list()
for i in a:
    b.append(i[2] + i[1] + i[0])
print(max(b))