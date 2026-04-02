x,y=map(int,input().split())
dbm={}
res=0
for i in range(1,x+1):
    dbm[i%5]=dbm.get(i%5,0)+1
for i in range(1,y+1):
    v = (5-(i%5)) % 5
    if v in dbm:
        res += dbm[v]
print(res)