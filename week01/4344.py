for _ in range(int(input())):
    a = list(map(int, input().split()))
    average = sum(a[1:]) / a[0]
    cnt = 0
    for i in a[1:]:
        if average < i:
            cnt += 1
    print('{:.3f}%'.format((cnt/a[0])*100))