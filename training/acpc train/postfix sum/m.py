from math import gcd
n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i-1])
for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i+1])
ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i]))
print(ans)