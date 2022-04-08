from sys import stdin
input = stdin.readline

n, c = map(int, input().split()) # 집의 개수, 공유기의 개수
house_arr = [int(input()) for _ in range(n)] # 집의 좌표
house_arr.sort() # 집의 좌표 정렬

def bin_search():
    start = 1 # 공유기를 설치할 수 있는 최소 거리
    end = house_arr[len(house_arr) - 1] - house_arr[0] # 공유기를 설치할 수 있는 최대 거리
    temp = 0
    
    while start <= end: # 공유기를 설치할 수 있는 최소 거리와 최대 거리가 교차 한다면 종료
        mid = (start + end) // 2 # 공유기 설치 거리
        house = house_arr[0] # 공유기 설치한 집
        cnt = 1 # 공유기 개수
        
        for i in house_arr: # 공유기 설치
            if i >= house + mid: # 공유기 설치한 집과 공유기 설치 거리를 더했을 때 집의 좌표가 크거나 같으면 설치 가능
                cnt += 1 # 공유기 설치 완료
                house = i # 마지막으로 공유기 설치한 집
                
        
        if cnt >= c: # 설치한 공유기가 설치 해야될 공유기보다 크거나 같을 때
            start = mid + 1
            temp = mid # 끝날 때는 무조건 여기로 들어오기 때문에 전의 찾았던 공유기 설치 거리 저장
        else: # 설치한 공유기가 설치 해야될 공유기보다 작을 때
            end = mid - 1
    return temp

print(bin_search())