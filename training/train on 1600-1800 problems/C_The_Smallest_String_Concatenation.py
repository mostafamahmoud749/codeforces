from functools import cmp_to_key

def way(x,y):
    if x+y>y+x: return 1
    elif x+y<y+x: return-1
    return 0

n=int(input())
res=[]
for _ in range(n):
    res.append(input())
res.sort(key=cmp_to_key(way))
print("".join(res))