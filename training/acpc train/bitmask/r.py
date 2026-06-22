n,k=map(int,input().split())
if n.bit_count()>k or k>n:
    print("NO")
else:
    res=[]
    while n>0:
        l=n&-n
        res.append(l)
        n-=l
    i=0
    while len(res)<k:
        if res[i]==1:
            i+=1
        else:
            res[i]=res[i]//2
            res.append(res[i])
    print("YES")
    print(*res)