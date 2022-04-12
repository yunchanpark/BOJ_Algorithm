from sys import stdin
input = stdin.readline

N, B = map(int, input().split()) # 행렬 크기, 제곱 수
A = [[*map(int, input().split())] for _ in range(N)] # 행렬

def multi(temp, temp1):
    n = len(temp)
    arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            a = 0
            for k in range(n):
                a += temp[i][k] * temp1[k][j]
            arr[i][j] = a % 1000
    return arr

def func(A, B):
    if B == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000 
        return A
    temp = func(A, B//2)
    if B % 2:
        return multi(multi(temp, temp), A)
    else:
        return multi(temp, temp)
for i in func(A, B):
    print(*i)