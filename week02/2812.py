from sys import stdin
input = stdin.readline

n, k = map(int, input().split()) # n자리 숫자, 숫자 제거할 개수
s = input().rstrip() # 숫자
temp = k
stack = []
for i in s:
    d = i
    if k == 0:
        stack.append(d)
    elif not stack:
        stack.append(d)
    else:
        while stack[-1] < d:
            stack.pop()
            k -= 1
            if k == 0 or not stack:
                break
        stack.append(d)
print("".join(map(str, stack[:n-temp])))