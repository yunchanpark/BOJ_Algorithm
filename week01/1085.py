a, b, c, d = map(int, input().split())
result = min(abs(a-0), abs(a-c), abs(b-0), abs(b-d))
print(result)