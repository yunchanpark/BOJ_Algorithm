from sys import stdin
import heapq
input = stdin.readline

K, N = map(int, input().split()) # K: 배열의 개수, N: 찾을 인덱스
arr = list(map(int, input().split())) # 입력 받은 소수 배열
heap = [] # 힙 배열

# 입력 받은 소수 배열을 힙 배열에 초기화
for i in arr:
    heapq.heappush(heap, i)
    
# 찾을 인덱스 까지 반복
for i in range(N):
    # 힙 배열에서 최소값을 빼줌
    num = heapq.heappop(heap)
    # 입력 받은 소수 배열 반복
    for j in arr:
        # 힙 배열에 소수의 곱을 넣어줌
        new = num * j
        heapq.heappush(heap, new)
        
        # 효율성을 위해 중복된 수는 아예 넣지 않기 위해 작성
        # 예를 들어 2*3을 했는데 다음에 3*2도 해주지 않게 하기 위해서와
        # 4*2와 6*2는 같은 12이다.
        # 쉽게 말해서 heap 계속 배수를 넣기 때문에 자신의 약수를 만나면 종료
        if num % j == 0: break
else: # 반복문이 다 끝났을 때
    print(num)