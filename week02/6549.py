from sys import stdin

input = stdin.readline

while True:
    # n: 직사각형의 수
    # arr: 직사각형 높이 배열
    n, *arr = list(map(int, input().split()))
    
    # 0이 입력되면 탈출
    if n == 0: break
    
    max_size = 0 # max_size: 직사각형 최대 크기
    stack = [] # 직사각형의 [높이, 너비]스택

    # 배열을 하나씩 꺼냄
    # idx: 인덱스
    # data: 배열의 값
    for data in arr:
        temp = 0 # 너비 저장할 임시 변수
        
        # stack이 비어있지 않고
        # stack 최상단 높이가 현재 높이보다 크다면
        while stack and stack[-1][0] > data:
            h = stack[-1][0] # stack 최상단의 높이
            w = stack[-1][1] # stack 최상단의 너비
            temp += w # 너비를 더해줌
            # 이전의 최대값과  현재(너비 * 높이) 비교 
            max_size = max(max_size, temp * h) 
            stack.pop()
        
        temp += 1
        stack.append([data, temp]) # stack에 [높이, 너비] 추가
    temp = 0
    while stack:
        temp += stack[-1][1]
        max_size = max(max_size, temp * stack[-1][0])
        stack.pop()
    print(max_size)