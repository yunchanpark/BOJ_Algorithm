from sys import stdin
input = stdin.readline

# 찾을 문자길이
n = int(input())

# 기본 S(0)의 문자 길이로 초기화
size = 3
# 몇 번째 수열인지 담는 변수
k = 1

# 문자길이를 찾을 수 있는 S(N)에서 N구하기
while True:
    size = (2*size) + k + 3
    if size >= n: break
    k += 1
# 문자 찾기
def moo(k, n, size):
    # 수열이 S(0)까지 쪼갰을 때
    if k == 0:
        if n == 1:
            return 'm'
        else:
            return 'o'
    size = (size - 3 - k) // 2
    if n <= size: # 첫 부분
        return moo(k-1, n, size)
    elif n <= size + k + 3: # 가운데 부분
        if n - size == 1:
            return 'm'
        return 'o'
    else: # 세번째 부분
        return moo(k-1, n - size - k - 3, size)
print(moo(k, n, size))
