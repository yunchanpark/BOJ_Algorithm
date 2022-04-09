from sys import stdin
input = stdin.readline

n = int(input()) # 막대기 개수
arr_h = [] # 막대기 높이 담을 배열

for _ in range(n):
    h = int(input())
    if not arr_h:
        arr_h.append(h)
    else:
        while arr_h and h >= arr_h[-1]:
            arr_h.pop()
            if not arr_h: break
        arr_h.append(h)
print(len(arr_h))