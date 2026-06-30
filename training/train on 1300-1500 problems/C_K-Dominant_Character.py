s=list(input().strip())
a=set(s)
res=float("inf")
for i in a:
    l=-1
    r=-1
    cres=0
    while r<len(s)-1:
        r+=1
        if s[r]==i:
            cres=max(cres,r-l)
            l=r
    cres=max(cres,len(s)-l)
    res=min(cres,res)
print(res)