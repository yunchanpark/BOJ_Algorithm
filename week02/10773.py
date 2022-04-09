from sys import stdin
input = stdin.readline

n = int(input()) # 입력할 정수의 개수
arr = [] # 입력한 정수 배열

for i in range(n):
    k = int(input()) # 입력한 수
    if k == 0 and len(arr) != 0: # 입력한 수가 0이 아니고 배열이 비어있지 않을 때
        arr.pop()
    else:
        arr.append(k)
print(sum(arr))