import sys
import math
a = list(map(int, sys.stdin.readline().split()))
temp = a[2] - a[0]
temp1 = a[0] - a[1]
b = math.ceil(temp / temp1)
print(b+1)