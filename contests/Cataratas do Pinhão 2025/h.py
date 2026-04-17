import math
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    lv=1
    rv=1
    for i in range(1,r+1):
        rv*=10
    for i in range(1,l):
        lv*=10
    print(math.ceil(rv**(.5))-math.ceil(lv**(.5)))
