a = int(input())
b = 0
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    b = 1
print(b)