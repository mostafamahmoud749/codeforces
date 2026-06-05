t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=[]          
    s=0
    for i in range(n-1,-1,-1):
        if s%2==0:
            if a[i]>0:
                res.append(i+1)
                s=+1
        else:
            if a[i]<0:
                res.append(i+1)
                s+=1
    print(len(res))
    print(*res)