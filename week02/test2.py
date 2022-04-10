from sys import stdin
input = stdin.readline

n = int(input())  # 원의 개수
arr = [list(map(int, input().split())) for _ in range(n)]  # 원의 정보[중심 좌표, 반지름]
stack = []  # 원의 시작점, 원의 끝점
for idx, data in enumerate(arr):  # x: 원의 중심, r: 원의 반지름
    arr[idx][0], arr[idx][1] = data[0] - \
        data[1], data[0] + data[1]  # 원의 시작 지점, 원의 끝 지점
arr.sort(key=lambda x: (x[0], -x[1]))  # 배열을 시작점은 오름차순, 만약 시작점이 같을 때는 내림차순
cnt = 1 + n  # 원의 개수가 최소 1개 이기 때문에 영역은 최소 2이상, 최소 원의 개수 만큼 영역이 있기 때문
'''
스택에 시작점, 끝점, 다음 원의 끝점
! 다음 원의 끝점이 있어야되는 이유는 원이 완벽하게 곂치기 않을 수도 있기 때문 
'''
if n == 1:  # 만약 원의 개수가 1개일 때
    print(cnt)
else:
    stack.append(arr[0] + [arr[0][1]])  # 스택에 제일 큰 원의 시작점과 끝점 + 다음 원의 끝점
    print(stack)
    for i in range(1, n):
        if stack[-1][0] == arr[i][0]: # 스택에 최상단 시작점과 현재 시작점이 같을 때
            if stack[-1][1] == arr[i][1]: # 스택에 최상단 끝점과 현재 끝점이 같을 때
                cnt += 1
            else:
                stack.append(arr[i] + [stack[-1][2]])
        elif stack[-1][1] == arr[i][0]:
            if arr[i][1] == stack[-1][2]:
                stack = []
                stack.append(arr[i] + [arr[i][1]])
                cnt += 1
            else:
                stack.append(arr[i] + [stack[-1][2]])
        else:
            stack.append(arr[i] + [arr[i][1]])
        print(stack)
    print(cnt)
