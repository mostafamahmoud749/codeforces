n=int(input())
a=list(input().strip())
c=len(set(a))
db={}
j=0
res=float("inf")
for i in range(n):
    db[a[i]]=db.get(a[i],0)+1
    while len(db)==c:
        res=min(res,i-j+1)
        db[a[j]]-=1
        if db[a[j]]==0:
            del db[a[j]]
        j+=1
print(res)