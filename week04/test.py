n, k = map(int, input().split())
data = []
D = [0] * (k+1)
for i in range(n):
    weight, value = map(int, input().split())
    data.append([weight, value])
data.sort()
for i in range(data[0][0], k+1):
    D[i] = data[0][1]
    
for i in range(1, len(data)):
    for j in range(data[i][0], k+1):
        if j-data[i][0] >= data[i][0]:
            D[j] = max(D[j], D[data[i][0]-1]+data[i][1])
        else:
            D[j] = max(D[j], D[j-data[i][0]]+data[i][1])
            
print(D[-1])
