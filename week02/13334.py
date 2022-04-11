from sys import stdin
import heapq

input = stdin.readline

n = int(input())
road_info = [list(map(int, input().split())) for _ in range(n)]

d = int(input())
roads = []

for road in road_info:
    house = road[0]
    office = road[1]
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        print(f'1. {heap}')
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap: break
        heapq.heappush(heap, road)
        print(f'2. {heap}')
    answer = max(answer, len(heap))
print(answer)