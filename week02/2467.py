from sys import stdin, stdout

N = int(input()) # 용액 개수
arr = sorted(tuple(map(int, stdin.readline().split())))  # 용액 배열

start, end = 0, N-1 # 시작점, 끝점
min_size = 2000000000 # 최솟값 저장할 변수
min_value, max_value = 0, 0
while start < end:
    temp = arr[start] + arr[end] # 시작점, 끝점 용액 섞은 값
    
    if min_size > abs(temp):
        min_value = arr[start]
        max_value = arr[end]
        min_size = abs(temp)
    
    if min_size == 0:
        break
    if temp < 0:
        start += 1
    else:
        end -= 1
stdout.write(f'{min_value} {max_value}')
