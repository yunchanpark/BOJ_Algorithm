import sys

a = int(sys.stdin.readline())

arr = [1] * 99

for i in range(100, 1000):
    if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
        arr.append(1)
    else:
        arr.append(0)

print(sum(arr[:a]))