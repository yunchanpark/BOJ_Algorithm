from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
k = int(input())
apples = []
for i in range(k):
    x, y = map(int, input().split())
    apples.append([x - 1, y - 1])
L = int(input())
turns = []
for i in range(L):
    turns.append(list(input().split()))
turns.sort(key=lambda x: -int(x[0]))
snake = deque()
snake.append((0, 0))
time = 0
state = 'x+'  # 'x+', 'x-', 'y+', 'y-'


def getApple(snake, apples):
    x, y = snake[-1]
    for apple in apples:
        if apple[0] == x and apple[1] == y:
            apples.remove(apple)
            return True
    return False


while True:
    head = snake[-1]
    hx = head[0]
    hy = head[1]
    if hx < 0 or hx > n - 1 or hy < 0 or hy > n - 1:
        break  # 1. 벽 부딪힐 때
    # 상태 변화 체크 L D.....
    if turns and time == int(turns[-1][0]):
        if state == "x+":
            if turns[-1][1] == 'L':
                state = "y-"
            else:
                state = 'y+'
        elif state == "x-":
            if turns[-1][1] == 'L':
                state = "y+"
            else:
                state = 'y-'
        elif state == "y+":
            if turns[-1][1] == 'L':
                state = "x+"
            else:
                state = 'x-'
        elif state == "y-":
            if turns[-1][1] == 'L':
                state = "x-"
            else:
                state = 'x+'
        turns.pop()
    print(
        f"head : {hx}, {hy} // time : {time} // state : {state} // snake : {snake}"
    )
    # 3. 이동
    if state == 'x+':
        if [hx, hy + 1] in snake:
            break  # 2. 자기 몸에 부딪힐 때
        snake.append((hx, hy + 1))
    elif state == 'x-':
        if [hx, hy - 1] in snake:
            break  # 2. 자기 몸에 부딪힐 때
        snake.append((hx, hy - 1))
    elif state == 'y+':  # 밑으로 내려감
        if [hx + 1, hy] in snake:
            break  # 2. 자기 몸에 부딪힐 때
        snake.append((hx + 1, hy))
    else:  # 위로 올라감
        if [hx - 1, hy] in snake:
            break  # 2. 자기 몸에 부딪힐 때
        snake.append((hx - 1, hy))
    if not getApple(snake, apples):
        snake.popleft()
    time += 1
print(time)
