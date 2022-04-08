import sys
input = sys.stdin.readline

def select1(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

n = int(input())
a = [int(input()) for _ in range(n)]
for i in select1(a):
    print(i)
