from sys import stdin
input = stdin.readline

K, N = map(int, input().split()) # 랜선의 개수, 필요한 랜선의 개수
arr = [int(input()) for _ in range(K)] # 랜선의 길이 배열
arr.sort() # 배열 정렬

start , end = 0, arr[-1]
result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2 # 가운데 랜선 길이

    # 랜선 길이로 mid로 나눈 몫을 cnt에 더함
    for i in arr:
        if mid != 0:
            cnt += i // mid

    # cnt가 필요한 것보다 많다면 짧게 짤랐다는 뜻이므로 start를 올려줌
    # cnt가 필요한 것보다 적다면 길게 짤랐다는 뜻이므로 end를 내려줌
    if cnt >= N:
        start = mid + 1
        result = mid
    else:
        end = mid -1
print(result)
