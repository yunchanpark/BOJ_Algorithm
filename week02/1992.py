from sys import stdin

input = stdin.readline

n = int(input())
arr = [input() for _ in range(n)]

def func(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                print('(', end='')
                func(x, y, n//2)
                func(x, y+n//2, n//2)
                func(x+n//2, y, n//2)
                func(x+n//2, y+n//2, n//2)
                print(')', end='')
                return
    else:
        print(color, end='')
func(0, 0, n)