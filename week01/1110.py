from sys import stdin
input = stdin.readline

n = int(input())
cnt = 0

if n < 10:
    s = '0' + str(n)
else:
    s = str(n)

while True:
    temp = int(s[0]) + int(s[1])
    temp = str(temp)
    s = s[1] + temp[len(temp)-1]
    cnt += 1
    if int(s) == n: break
print(cnt)