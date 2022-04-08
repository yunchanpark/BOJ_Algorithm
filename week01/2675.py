import sys
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().split()
    for i in a[1]:
        temp = ''
        for j in range(int(a[0])):
            temp += i
        print(temp, end='')
    print()