t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(map(int,input().split()))
    b=[]
    for i in range(n):
        if a[i]>=2:
            b.append(a[i])
    if len(b)==0:
        res=0
    elif len(b)==1:
        res=b[0]+min(n-1,b[0]//2)
    else:
        mid=0
        for i in range(len(b)):
            mid+=(b[i]-2)//2
        res=sum(b)+min(n-len(b),mid)
    if res<3:
        res=0
    print(res)