import math

# 

n=int(input())
a=sorted(map(int,input().split()))


if n==1:
    print(1)
else:

    g=math.lcm(a[0],a[1])
    for i in range(1,n):
        g=math.lcm(g,a[i])

    res=0
    # print(g)
    for i in range(n):
        res+=g//a[i]
    print(res)
