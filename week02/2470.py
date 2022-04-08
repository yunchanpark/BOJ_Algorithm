from sys import stdin
input = stdin.readline

n = int(input()) # 전체 용액 수
arr = list(map(int, input().split())) # 용액의 특성값
arr.sort() # 용액의 특성값 정렬
size = len(arr) - 1 # 배열의 길이

def bin_search():
    start = 0 # 시작 인덱스
    end = len(arr) - 1 # 끝 인덱스
    max_value, min_value = 0, 0  # 최솟값 최대값 섞은 값
    answer = 2000000000 # 기준값
    
    while start < end: # 시작 인덱스와 끝 인덱스가 교차하면 종료
        mix = arr[start] + arr[end]  # 최솟값과 최대값을 더한 절댓값을 담아 준다.
        if  abs(mix) < abs(answer):
            min_value, max_value = arr[start], arr[end]  # 최솟값, 최대값 초기화
            answer = mix
        if mix == 0:  # 섞은 용액 값이 0일 때
            break
        if mix > 0:  # 섞은 용액 값이 0보다 크거나 같을 때
            end -= 1
        else: # 섞은 용액 값이 0보다 작을 때
            start += 1
    print(min_value, max_value)

if arr[size] <= 0: # 배열의 최대값이 음수 일 때, 즉, 배열의 모든 값이 음수
    print(arr[size - 1], arr[size])
elif arr[0] >= 0: # 배열의 최솟값이 양수 일 때, 즉, 배열의 모든 값이 양수
    print(arr[0], arr[1])
else: # 즉, 배열의 값이 음수와 양수가 섞여 있을 때
    bin_search()