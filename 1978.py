import sys

def 소수(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cnt = int(sys.stdin.readline())
arrList = list(map(int, sys.stdin.readline().split()))
result = 0

for i in arrList:
    if 소수(i):
        result += 1
print(result)