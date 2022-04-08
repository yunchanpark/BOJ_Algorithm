from sys import stdin
input = stdin.readline
n = int(input())


def hanoi(a, b, n):
    if n == 1:
        print(a, b)
        return

    hanoi(a, 6-a-b, n-1)
    print(a, b)
    hanoi(6-a-b, b, n-1)
    return


print(2**n-1)
if n <= 20:
    hanoi(1, 3, n)