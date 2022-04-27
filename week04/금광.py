from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [[arr[i] for i in range(j * m, (j * m) + m)] for j in range(n)]
    
    print(*arr, sep='\n')
    for j in range(1, m):
        for i in range(n):
            if i == 0: left_up = 0
            else: left_up = arr[i - 1][j - 1]
            if i == n - 1: left_down = 0
            else: left_down = arr[i + 1][j - 1]
            left = arr[i][j - 1]
            arr[i][j] = arr[i][j] + max(left, left_down, left_up)
    result = 0
    for i in range(n):
        result = max(result, arr[i][m - 1])
    print(result)