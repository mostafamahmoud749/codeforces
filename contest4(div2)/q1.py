import math
t=int(input())
for _ in range(t):
    n,m,d=map(int,input().split())
    res=(d//m)+1
    if res==0:

        print(n)
    else:
        print(math.ceil(n/res))
