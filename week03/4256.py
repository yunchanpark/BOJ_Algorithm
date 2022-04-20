from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = stdin.readline

def postorderset(preorder, inorder):
    if len(preorder) == 0: return
    if len(preorder) == 1: return
    # 루트
    root = preorder[0]
    root_idx = inorder.index(root)
    
    postorderset(preorder[1:root_idx+1], inorder[:root_idx])
    postorderset(preorder[root_idx+1:], inorder[root_idx+1:])
    print(root, end=' ')
    
# 테스트 케이스
T = int(input())
for _ in range(T):
    # 노드 개수
    n = int(input())
    # 전위 순회 값
    preorder = list(map(int, input().split()))
    # 중위 순회 값
    inorder = list(map(int, input().split()))
    # 후위 순회로 바꿈
    postorderset(preorder, inorder)
    print()
