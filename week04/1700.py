from sys import stdin
input = stdin.readline

N, K = map(int, input().split()) # 멀티탭 구멍개수, 전기 용품 총 사용횟수

arr = list(map(int, input().split())) # 플러그 이름
multi = [] # 멀티탭
holes = N # 멀티탭 구멍
start = 0 # 플러그 시작 인덱스
cnt = 0 # 플러그 뺀 개수

# 인덱스 찾기
def index(start, value):
    for i in range(start, K):
        if arr[i] == value:
            return i
    return -1

# 처음에 멀티탭 다 연결될 때 까지 초기화
while holes > 0:
    if arr[start] not in multi:
        multi.append(arr[start])
        holes -= 1
    start += 1

# 멀티탭에 다 꽂은 후 하나씩 돌면서 갈아 끼움
for i in range(start, K-1):
    # 현재 플러그가 멀티탭에 있을 때
    if arr[i] in multi: continue
    
    # 멀티탭에 있는 플러그 중에 제일 나중에 나오는 플러그
    max_idex = -1e9
    # 뽑을 플러그 
    remove_data = None
    
    # 멀티탭에 있는 플러그 인덱스 검사
    # 제일 나중에 나오는 플러그 삭제
    for data in multi:
        temp = index(i+1, data)
        if max_idex < temp:
            max_idex = temp
            remove_data = data
        if temp == -1:
            multi.remove(data)
            break
    else:
        multi.remove(remove_data)
    
    # 뽑을 개수 올려줌
    cnt += 1
    # 멀티탭에 현재 플러그 꽂음
    multi.append(arr[i])
    
if arr[K-1] not in multi: cnt += 1
print(cnt)