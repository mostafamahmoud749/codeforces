import math
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    g = math.gcd(a, b)
    if a//g<=k and b//g<=k:
        print(1)
    else:
        print(2)