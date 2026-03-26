import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n, x = data[0], data[1]
db={}
a=data[2:2+n]
s=False
v=[]
for i in range(n):
    r=x-a[i]
    if db.get(r) is not None:
        s=True
        v.append(db[r]+1)
        v.append(i+1)
        break
    else:
        db[a[i]]=i
if s:
    print(v[0],v[1])
else:
    print("IMPOSSIBLE")
