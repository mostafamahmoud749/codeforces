t=int(input())
for i in range(t):
    y=input()
    x=list(map(int,input().split()))
    comp=min(x)
    res=0
    for k in x:
        if k>comp:
            res+=k-comp
    print(res)