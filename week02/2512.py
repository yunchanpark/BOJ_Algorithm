from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 0, max(arr)
result = 0
while start <= end:
    temp = 0
    mid = (start + end) // 2
    for i in arr:
        if i <= mid:
            temp += i
        else:
            temp += mid
    
    if temp <= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
