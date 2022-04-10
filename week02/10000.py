from sys import stdin
input = stdin.readline

n = int(input()) # 원의 개수
arr = [list(map(int, input().split())) for _ in range(n)] # 원의 정보[중심 좌표, 반지름]
stack = [] # 원의 시작점, 원의 끝점
cnt = 1 + n # 영역은 최소 1이상 때문, 최소 원의 개수 만큼 영역이 있기 때문
for idx, data in enumerate(arr):  # x: 원의 중심, r: 원의 반지름
    arr[idx][0], arr[idx][1] = data[0] - data[1], data[0] + data[1]  # 원의 시작 지점, 원의 끝 지점
arr.sort(key=lambda x: (x[0], -x[1])) # 원의 시작점은 오름차순으로 정렬하고, 시작점이 같은 경우는 끝 점을 내림차순으로 정렬
stack.append(arr[0]) # 스택에 제일 큰 원의 인덱스 추가

for i in range(1, n):
    if stack[-1][1] <= arr[i][0]: # 만약에 스택 최상단에 있는 원의 끝점보다 현재 원의 시작점이 크거나 같다면
        stack.pop()
    if stack:
        for j in range(len(stack)-1, -1, -1):
            if stack[j][0] in arr[i]:  # 만약에 스택에 있는 시작점이 현재 원의 시작점이나 끝점하고 곂치면 방문처리
                stack[j][0] = True # 시작점 곂친 표시
            elif stack[j][1] in arr[i]:  # 만약에 스택에 있는 끝점이 현재 원의 시작점이나 끝점하고 곂치면 방문처리
                stack[j][1] = True # 끝점 곂친 표시
            if stack[j][0] == True and stack[j][1] == True: # 시작점과 끝점이 곂쳐 있으면 
                stack.pop(j) # 스택에 들어있는 해당 원을 팝
                cnt += 1 # 영역 하나 추가
    stack.append(arr[i]) # 스택에 현재 원의 인덱스 추가
print(cnt)