import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    s=[0]*n
    for i in range(n):
        s[i]=int(input())
    s.sort()
    l=0
    r=s[-1]-s[0]
    res=0
    while l<=r:
        mid=l+(r-l)//2
        j=0
        curc=1
        for i in range(1, n):
            if s[i]-s[j]>=mid:
                curc+=1
                j=i
        if curc>=c:
            res=mid
            l=mid+1
        else:
            r=mid-1
    print(res)
