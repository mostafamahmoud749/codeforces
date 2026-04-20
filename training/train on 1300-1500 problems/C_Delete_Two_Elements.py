t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if (sum(a)*2)%n!=0:
        print(0)
        continue
    v=(sum(a)*2)//n
    db={}
    res=0
    for i in range(n):
        db[a[i]]=db.get(a[i],0)+1
    a=set(a)
    a=list(a)
    for i in a:
        if v-i==i:
            res += db[i] * (db[i]-1)//2
        elif v-i>i:
            res+=db[i]*db.get(v-i,0)
    print(res)