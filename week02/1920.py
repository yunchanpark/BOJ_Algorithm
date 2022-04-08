from sys import stdin
input = stdin.readline
n = int(input()) # 원소 개수
arr = list(map(int, input().split())) # 원소 배열

m = int(input()) # 키 개수
keys = list(map(int, input().split())) # 키 배열
arr.sort() # 키 정렬

def bin_search(arr, key):
    pl = 0 # 인덱스 시작점
    pr = len(arr) - 1 # 인덱스 끝점
    
    while True:
        pc = (pl + pr) // 2 # 인덱스 중앙
        if arr[pc] == key: return 1  # 검색 성공
        elif arr[pc] > key: pr = pc - 1 # 만약 키값이 배열의 중앙보다 작으면 끝점을 이동 
        else: pl = pc + 1  # 만약 키값이 배열의 중앙보다 작으면 시작점을 이동
        if pl > pr: break
    return 0 # 검색 실패
for i in keys: print(bin_search(arr, i))