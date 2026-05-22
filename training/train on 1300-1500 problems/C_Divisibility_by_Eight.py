def genrate(indx,cs):
    global res,s
    if cs and int(cs)%8==0:
        res=cs
        s=True
        return
    if s or indx==len(n) or len(cs)==3:
        return
    genrate(indx+1,cs+n[indx])
    genrate(indx+1,cs)

n=input().strip()
res=-1
s=False
genrate(0, "")
if res!=-1:
    print("YES")
    print(res)
else:
    print("NO")
