from sys import stdin
input = stdin.readline
temp = 0
for i in range(8):
    s = input().strip()
    for j in range(len(s)):
        if i % 2 == 0 and j % 2 == 0 and s[j] == 'F':
            temp += 1
        elif i % 2 == 1 and j % 2 == 1 and s[j] == 'F':
            temp += 1
print(temp)