n=int(input())
a=list(map(int,input().split()))
db={}
res=0
for i in range(n):
    db[a[i]]=db.get(a[i],0)+1
while len(db)>0:
    cur=-float("inf")
    el=""
    for key in db:
        if cur<(db[key]*key)-((db.get(key-1,0)*(key-1)+db.get(key+1,0)*(key+1))):
            el=key
            cur=(db[key]*key)-((db.get(key-1,0)*(key-1)+db.get(key+1,0)*(key+1)))
    res+=db[el]*el
    db.pop(el-1,None)
    db.pop(el+1,None)
    db.pop(el)
print(res)