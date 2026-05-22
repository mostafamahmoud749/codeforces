t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    sa=sum(a)
    if s<sa:
        print(*a)
    elif s==sa:
        print(-1)
    else:
        if s-sa==1:
            c0=a.count(0)
            c1=a.count(1)
            c2=a.count(2)
            print(*([0]*c0+[2]*c2+[1]*c1))
        else:
            print(-1)

