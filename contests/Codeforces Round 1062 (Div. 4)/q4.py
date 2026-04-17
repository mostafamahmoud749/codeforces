import math
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    g=math.gcd(*a)
    x = 2
    while math.gcd(g, x) != 1:
        x += 1
    print(x)