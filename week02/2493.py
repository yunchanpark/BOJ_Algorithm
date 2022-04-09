from sys import stdin
input = stdin.readline

n = int(input()) # 탑의 수
arr = list(map(int, input().split())) # 탑 배열
stack = []
result = [0]*n

for i in range(n-1):
    if arr[i] < arr[i+1]:                       # 다음 값이 현재 값보다 클때
        if not stack:                               # 스택이 비어 있을 때
            stack.append(i+1)                           # 스택에 다음 값의 인덱스 추가
        else:                                       # 스택이 비어 있지 않을 때
            if arr[stack[-1]] > arr[i+1]:               # 스택의 마지막 값이 다음 값보다 클 때
                # print(i, i+1)
                # print(stack, arr[i], arr[i+1])
                result[i+1] = stack[-1] + 1                 # 스택의 마지막 값(인덱스)을 다음 값 인덱스에 추가
                stack.append(i+1)                           # 스택에 다음 인덱스를 추가
            elif arr[stack[-1]] == arr[i+1]:
                result[i+1] = stack[-1] + 1                 # 스택의 마지막 값(인덱스)을 다음 값 인덱스에 추가
            else:                                       # 스택의 마지막 값이 다음 값보다 작을 때
                # print(arr[stack[-1]], arr[i+1])
                # print(stack, arr[i], arr[i+1])
                stack.pop()                                 # 스택의 마지막 값을 pop
                if stack:
                    result[i+1] = stack[-1] + 1                 # 스택의 마지막 값(인덱스)을 다음 값 인덱스에 추가
    else:                                        # 다음 값이 현재 값보다 작을 때
        if not stack:
            stack.append(i)
        else:
            if stack[-1] != i:
                stack.append(i)
        result[i+1] = i+1
print(*result)