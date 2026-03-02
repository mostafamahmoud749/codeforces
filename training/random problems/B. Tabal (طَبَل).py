t=int(input())
for j in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=0
    x={}
    y={}
    for i in a:
        if i in x:
            x[i]+=1
        else:
            x[i]=1
    for i in b:
        if i in y:
            y[i]+=1
        else:
            y[i]=1
    for l in y:
        if l in x:
            res+=min(y[l],x[l])
    print(res)

    
    
    
