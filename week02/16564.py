from sys import stdin
from unittest import result
input = stdin.readline

n, k = map(int, input().split()) # 캐릭터의 개수, 올릴 수 있는 레벨 총합
arr = [int(input()) for _ in range(n)] # 각각의 캐릭터의 레벨
arr.sort() # 배열 정렬

def bin_search():
    start = arr[0] # 최소 레벨
    end = arr[n-1] + k # 최대 레벨 + 올릴 수 있는 레벨 총합
    result = 0
    while start <= end:
        temp = 0 
        mid = (start + end) // 2 # 최소 레벨과 최대 레벨사이의 가운데
        for i in arr:
            if i < mid: # 가운데 레벨보다 작을 때
                temp += mid - i # 가운데 레벨에서 현재 레벨은 빼준 값을 더함
        # 다 더한 값들이 
        if temp <= k: 
            result = mid
            start = mid+1  # 올릴 수 있는 레벨 총합보다 작다면 기준이 작다라는 뜻이기 때문에 시작점을 올려준다
        else: end = mid-1 # 올릴 수 있는 레벨 총합보다 크다면 기준이 크다는 뜻이기 때문에 끝 점을 내려준다
    return result
print(bin_search())