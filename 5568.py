import sys
input = sys.stdin.readline

# 총 카드 수
n = int(input())
# 카드 선택 개수
k = int(input())
# 카드 리스트
arr = [input().strip() for _ in range(n)]
# 체크
check = [0]*n
# 조합 카드
temp = []
# 중복없는 카드
result = set()

def card(N):
    if N == k:
        result.add(''.join(temp))
        return

    for i in range(n):
        if check[i]:
            continue
        check[i] = 1
        temp.append(arr[i])
        card(N+1)
        check[i] = 0
        temp.pop()

card(0)
print(len(result))