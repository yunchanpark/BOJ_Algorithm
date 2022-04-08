import sys

def 소수(n):
    for i in n:
        if i == 1:
            return False
        if i == 2:
            continue
        if i % 2 != 0:
            for j in range(2, int((i**0.5))+1):
                if i % j == 0:
                    return False
        else:
            return False
    return True


for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    temp = []
    result = ''
    for j in range(1, num//2+1):
        a = list()
        a.append(j)
        a.append(num-j)
        if 소수(a):
            if len(temp) == 0:
                result = str(a[0]) + ' ' + str(a[1])
                temp.append(a)
            else:
                result = str(temp[0][0]) + ' ' + str(temp[0][1]) if abs(
                    temp[0][0] - temp[0][1]) < abs(a[0] - a[1]) else str(a[0]) + ' ' + str(a[1])
    print(result)