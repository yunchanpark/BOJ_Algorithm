from inspect import stack
from sys import stdin

input = stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0: break
    if arr[0] == 1:
        print(arr[1])
        break
    if arr[0] == 2:
        print(min(arr[1:])*2)
        break
    stack = []
    stack.append(arr[1])
    for i in range(2, len(arr)):
        if stack[-1] < arr[i]:
            stack.pop()
        stack.append(arr[i])