from sys import stdin
input = stdin.readline
n = int(input())
cnt = 0
arr = [0]*n
check1 = [0]*n
check2 = [0]*(n*2-1)
check3 = [0]*(n*2-1)


def queen(k):
    global cnt
    if k == n:
        cnt += 1
        return
    for i in range(n):
        if not check1[i] and not check2[i+k] and not check3[k-i+n-1]:
            check1[i] = check2[k+i] = check3[k-i+n-1] = 1
            queen(k+1)
            check1[i] = check2[k+i] = check3[k-i+n-1] = 0
    return cnt


print(queen(0))