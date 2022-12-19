a, b, c, d = map(int, input().split())
if d > b:
    ans = a + c*(d-b)
else:
    ans = a
print(ans)
