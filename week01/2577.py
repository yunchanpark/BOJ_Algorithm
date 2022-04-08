import sys
temp = 1
dic = {}

for _ in range(3):
    a = sys.stdin.readline()
    temp *= int(a)

for i in range(10):
    dic[i] = 0

for i in str(temp):
    dic[int(i)] = dic[int(i)] + 1

for i in dic.values():
    print(i)
