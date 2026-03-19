n,m=map(int,input().split())
v=[0]*n
db=[[] for _ in range(n)]

for i in range(m):
    l,r=map(int,input().split())
    db[l-1].append(r-1)
    db[r-1].append(l-1)

for i in range(n):
    used = set()
    for j in db[i]:
        if v[j] != 0:
            used.add(v[j])
    for k in range(1, 5):
        if k not in used:
            v[i] = k
            break
    
print(''.join(map(str, v)))