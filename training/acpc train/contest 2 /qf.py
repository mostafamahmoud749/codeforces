n,k=map(int,input().split())
res=0
for i in range(n):
    a=input()
    db=[-1]*(k+1)
    for i in range(len(a)):
        if int(a[i])>k:
            continue
        db[int(a[i])-1]=1
    if db.count(1)==k+1:
        res+=1

print(res)