# 시간이 훨씬 단축되는 코드
# 링크: https://www.acmicpc.net/source/30813571
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def pre_to_post(start, end):
    if start > end:
        return

    root = preorder[start]  # 전위 순회는 루트를 가장 먼저 탐색
    idx = end + 1
    # 루트 왼쪽에만 자식이 있을 때
    # 이 코드가 시간을 아주 많이 단축시킴
    # if preorder[end] <= root:
    #     pre_to_post(start + 1, end)
    #     print(root)
    #     return

    # 오른쪽 자식이 시작되는 위치를 찾음
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            idx = i
            break

    pre_to_post(start + 1, idx - 1)  # 왼쪽 서브 트리 탐색
    print(root)
    pre_to_post(idx, end)  # 오른쪽 서브 트리 탐색


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
pre_to_post(0, len(preorder) - 1)