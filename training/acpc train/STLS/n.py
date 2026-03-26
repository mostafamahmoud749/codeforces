n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
db={}
res=0

for j in range(n):
    val=b[c[j]-1]
    db[val]=db.get(val,0)+1

for i in range(n):
    res+=db.get(a[i],0)

print(res)