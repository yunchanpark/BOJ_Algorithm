from sys import stdin
input = stdin.readline

n, m = map(int, stdin.readline().split()) # 나무 수, 나무 길이
h = list(map(int, stdin.readline().split())) # 나무 높이

start, end = 0, max(h)

while start <= end:
    temp = 0
    cut_h = (start + end) // 2
    
    for i in h:
        if i > cut_h:
            temp += i - cut_h
    if temp >= m:
        start = cut_h + 1
    else:
        end = cut_h - 1
print(end)
