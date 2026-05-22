def get(idx, cw):
    if idx == n or cw == 0:
        return 0
    res=get(idx+1,cw)
    if items[idx][1]<=cw:
        res=max(res,get(idx+1,cw-items[idx][1])+items[idx][0])
    return res

n,w=map(int,input().split())
items=[]
for i in range(n):
    iw,iv=map(int,input().split())
    items.append([iv,iw])

res=get(0, w)
print(res)