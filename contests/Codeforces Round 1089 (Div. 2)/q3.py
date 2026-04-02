import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=0
    g1=math.gcd(a[0],a[1])
    if g1<a[0]:
        res+=1
        a[0]=g1
    for i in range(1,n-1):
        v=math.lcm(math.gcd(a[i],a[i-1]),math.gcd(a[i],a[i+1]))
        if v<a[i]:
            res+=1
            a[i]=v
    g2=math.gcd(a[-1],a[-2])
    if g2<a[-1]:
        res+=1
    print(res)