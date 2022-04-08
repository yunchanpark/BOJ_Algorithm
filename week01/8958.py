for i in range(int(input())):
    sum = 0
    cnt = 0
    a = input()
    for j in a:
        if j == 'O':
            sum += cnt
            sum += 1
            cnt += 1
        else:
            cnt = 0
    print(sum)