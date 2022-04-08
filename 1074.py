# from sys import stdin
# input = stdin.readline
# n, r, c = map(int, input().split())

# def f(n, r, c):
#     if n == 0:
#         return 0
#     return 2*(r % 2)+(c % 2) + 4*f(n-1, int(r/2), int(c/2))

# print(f(n, r, c))

from sys import stdin
input = stdin.readline
n, r, c = map(int, input().split())

result = 0

def func(n, r, c):
    global result
    half = (2**n)//2
    if n == 0:
        print(result)
        return

    if r < half and c < half:  # 1사분면
        func(n-1, r, c)
    elif r < half and c >= half:  # 2사분면
        result += half**2
        func(n-1, r, c-half)
    elif r >= half and c < half:  # 3사분면
        result += half**2*2
        func(n-1, r-n, c)
    elif r >= half and c >= half:  # 4사분면
        result += half**2*3
        func(n-1, r-half, c-half)

func(n, r, c)