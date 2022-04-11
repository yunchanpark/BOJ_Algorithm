from sys import stdin
input = stdin.readline

n = int(input()) # 탑의 수
arr = list(map(int, input().split())) # 탑 배열
stack = []
result = [0]*n

stack.append(0)
for i in range(1, n):
    while stack:
        if arr[stack[-1]] > arr[i]:
            result[i] = stack[-1] + 1
            break
        else:
            stack.pop()
    stack.append(i)
print(*result)