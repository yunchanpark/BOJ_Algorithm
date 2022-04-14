from sys import stdin, stdout
input = stdin.readline
print = stdout.write

str = input().rstrip()  # 입력 문자열
boom = input().rstrip()  # 폭발 문자열
boom_end = boom[-1]  # 폭발 문자열 끝 문자
boom_size = len(boom)  # 폭발 문자열 크기
result = []  # 스택 배열

# 입력 문자열을 하나씩 꺼내여 반복
# 스택에 추가
for s in str:
    result.append(s)
    
    # 현재 문자와 폭발 문자열의 끝자리가 같고 
    # 스택에서 폭발 문자열의 길이 만큼 뺀 문자열이 폭발 문자열과 같으면
    # 폭발 문자열 길이 만큼 pop
    if s == boom_end and "".join(result[-boom_size:]) == boom:
        for _ in range(boom_size): result.pop()

# 스택이 비어있지 않다면 문자열 연결
# 스택이 비어있다면 FRULA 출력
if result:
    print("".join(result))
else:
    print("FRULA")