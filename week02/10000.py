# 10000 원 영역
import sys
# input = sys.stdin.readline
N = int(input())
circles = []
for _ in range(N):
    x, r = map(int, input().split())
    circles.append((x-r, x+r))
circles.sort(key=lambda x: (x[0], -x[1]))
region_num = N + 1  # 영역 수
parent_stack = []  # 부모만 저장 -> 그렇기 때문에 class가 구분됨.
class_linkage_stack = []  # 클래스별 자식들이 연결됐는지 여부 정보 저장
for now_start, now_end in circles:
    if parent_stack:  # 바로 부모를 만나는 경우 대비
        prev_start, prev_end = parent_stack[-1]
    while parent_stack and parent_stack[-1][1] < now_end:  # 부모의 자격이 없는 애들 탈락
        # 길이가 같을 때만 연결 정보 제거(자식이 없었던 부모는 연결정보가 없기 때문에 확인)
        if len(parent_stack) == len(class_linkage_stack):
            class_linkage_stack.pop()
        prev_start, prev_end = parent_stack.pop()  # 탈락한 부모는 이전 원이 됨
    if not parent_stack:  # parent_stack이 비어 있다면 현재 원을 append해주고 다음 원으로
        parent_stack.append((now_start, now_end))
    else:  # parent_stack에 뭔가 있다면
        parent_start, parent_end = parent_stack[-1]  # 현재 보는 원의 부모
        parent_stack.append((now_start, now_end))  # 현재 원 일단 부모로 넣어주기
        if prev_end == parent_end:  # 이전 원이 현재 원의 부모였던 경우
            if now_start == prev_start:  # 부모 원과 연결되면서 시작
                class_linkage_stack.append(True)
            else:
                class_linkage_stack.append(False)
        else:  # 이전 원과 나란히 있는 경우(이전 원이 부모가 아닌 경우)
            if prev_end == now_start:  # 이전 원과 나란히 이어지는 경우
                # 완전히 부모 원과 이어진 경우
                if now_end == parent_end and class_linkage_stack[-1]:
                    region_num += 1
            else:  # 이전 원과 떨어져 있는 경우
                class_linkage_stack[-1] = False
print(region_num)