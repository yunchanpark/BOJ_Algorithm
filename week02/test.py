from sys import stdin
input = stdin.readline

n = int(input())  # 원의 개수
arr = [list(map(int, input().split())) for _ in range(n)]  # 원의 정보[중심 좌표, 반지름]
stack = []  # 원의 시작점, 원의 끝점
for idx, data in enumerate(arr):  # x: 원의 중심, r: 원의 반지름
    arr[idx][0], arr[idx][1] = data[0] - data[1], data[0] + data[1]  # 원의 시작 지점, 원의 끝 지점
arr.sort(key=lambda x: (x[0], -x[1])) # 배열을 시작점은 오름차순, 만약 시작점이 같을 때는 내림차순
cnt = 1 + n # 원의 개수가 최소 1개 이기 때문에 영역은 최소 2이상, 최소 원의 개수 만큼 영역이 있기 때문
'''
스택에 시작점, 끝점, 다음 원의 끝점
! 다음 원의 끝점이 있어야되는 이유는 원이 완벽하게 곂치기 않을 수도 있기 때문 
'''
print(arr)
if n == 1: # 만약 원의 개수가 1개일 때
    print(cnt)
else:
    stack.append(arr[0] + [arr[1][1]])  # 스택에 제일 큰 원의 시작점과 끝점 + 다음 원의 끝점
    for i in range(1, n):
        print(stack)
        if stack[-1][1] < arr[i][0]:  # 만약에 스택 최상단에 있는 원의 끝점보다 현재 원의 시작점이 크거나 같다면
            print(stack)
            stack.pop()
        if stack: # 위에서 pop을 하고 스택이 없을 수도 있기 때문
            if stack[-1][0] != arr[i][0]: 
                if stack[-1][2] < arr[i][0]: 
                    stack.pop()
        if stack:  # 위에서 pop을 하고 스택이 없을 수도 있기 때문
            if stack[-1][0] in arr[i]: # 만약에 스택 최상단의 시작점이 현재 원의 시작점과 곂치면
                stack[-1][0] = True
            if stack[-1][1] in arr[i]: # 만약에 스택 최상단의 끝점이 현재 원의 끝점과 곂치면
                stack[-1][1] = True
            if stack[-1][0] == True and stack[-1][1] == True:  # 시작점과 끝점이 곂쳐 있으면
                stack.pop()  # 스택에 들어있는 해당 원을 팝
                cnt += 1  # 영역 하나 추가
        if i < n-1:
            stack.append(arr[i] + [arr[i+1][1]]) 
    print(cnt)
