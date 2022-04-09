from sys import stdin
input = stdin.readline

n = int(input()) # 입력x할 수

def check(s):
    stack = [] # 왼쪽 괄호 담을 배열
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                a = stack.pop()
                if a != '(':
                    return False
            else:
                return False
    return False if stack else True

for _ in range(n):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')
