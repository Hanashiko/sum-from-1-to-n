n = int(input())
m = abs(n)
if m % 2 == 0:
    ans = m // 2 * (m + 1)
else:
    ans = (m + 1) // 2 * m
if n > 0:
    print(ans)
else:
    print(1 - ans)
