from sys import stdin
input = stdin.readline

A, B, C = map(int, input().split())

def func(A, B):
    if B == 1:
        return A % C
    else:
        temp = func(A, B//2)
        if B % 2 == 0:
            return (temp * temp) % C
        else:
            return (temp * temp * A) % C
print(func(A, B))