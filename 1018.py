from sys import stdin
input = stdin.readline

n = int(input())
s = input().rstrip()
sum = 0
for i in range(n):
    sum += int(s[i])
print(sum)