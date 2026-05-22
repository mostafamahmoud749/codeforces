def genrate(n,indx):
    if indx==ln:
        if n!="":
            p.add(int(n))
        return
    genrate(n+"4",indx+1)
    genrate(n+"7",indx+1)
    genrate(n,indx+1)

l,r=map(int,input().split())
ln=10
p=set()
genrate("",0)
p=list(p)
p.sort()
res=0
curr=l
for x in p:
    if x>=curr:
        res+=(min(x,r)-curr+1)*x
        curr=x+1
        if curr>r:
            break
print(res)