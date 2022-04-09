from sys import stdin

input = stdin.readline

n = int(input()) # 명령수
stack = [] # 수 넣어 둘 배열

for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])