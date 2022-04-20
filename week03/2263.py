from re import I
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline

# 노드 개수
n = int(input())
# 중위 순회 결과 값
inorder = list(map(int, input().split()))
# 후위 순회 결과 값
postorder = list(map(int, input().split()))
# 중위 순회 각 노드 인덱스 
index = [0] * (n + 1)
for i in range(n):
    index[inorder[i]] = i
    
# 전위 순회로 바꾸는 함수
def preorderset(inStart, inEnd, poStart, poEnd):
    if inStart > inEnd or poStart > poEnd: return
    
    # 트리의 루트
    root = postorder[poEnd]
    # 루트의 인덱스
    root_idx = index[root]
    # 전위 순회는 '루트-왼쪽-오른쪽'이기 때문에 바로 루트 출력
    print(root, end=' ')
    
    # 왼쪽 노드 개수
    left = root_idx - inStart
    # 오른쪽 노드 개수
    right = inEnd - root_idx
    
    # 왼쪽 트리 재귀
    preorderset(inStart, root_idx - 1, poStart, poStart + left - 1)
    # 오른쪽 트리 재귀
    preorderset(root_idx + 1, inEnd, poEnd - right, poEnd - 1)

preorderset(0, n - 1, 0, n - 1)