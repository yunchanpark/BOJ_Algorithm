from sys import stdin
# 입력, 출력
input = stdin.readline

n = int(input()) # 점의 개수

# 점의 [x, y] 좌표 배열
# x 좌표 기준으로 정렬
dot_arr = sorted(tuple(map(int, input().split())) for _ in range(n))
dot_arr.sort()
start, end = 0, n # 시작 인덱스, 끝 인덱스
min_size = float('inf')

# (x1-x2)^2 + (y1-y2)^2 = c^2
# 두 점의 거리의 제곱을 출력하기 때문에 루트 처리는 안함
# 두 점의 거리 구하는 공식
def distance(dot1, dot2):
    return (dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2

# 두 점 최소 거리 계산
# 병합
def marge(start, end, min_size):
    for i in range(start, end):
        for j in range(i+1, end):
            min_size = min(min_size, distance(dot_arr[i], dot_arr[j]))
    return min_size

# 분할
def divied(start, end, min_size):
    
    if start == end:
        return min_size
    # 종료 조건
    # 만약 분할해서 남은 개수가 2개 또는 3개라면(3개는 홀수 일때 하나로는 거리를 구할 수 없기 때문)
    if end - start + 1 < 4:
        return marge(start, end, min_size)
    
    mid = (start + end) // 2 # 인덱스 중앙값
    
    # 왼쪽 = 시작점 ~ 중앙값
    # 오른쪽 = 중앙값 ~ 끝값
    left = divied(start, mid, min_size)
    right = divied(mid, end, min_size)
    
    # 왼쪽의 최솟값과 오른쪽의 최솟값중에서 최솟값 구하기
    min_size = min(left, right)
    return min_size

print(divied(start, end, min_size))
