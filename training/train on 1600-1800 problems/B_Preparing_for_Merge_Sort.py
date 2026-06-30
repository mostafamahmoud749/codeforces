n=int(input())
a=list(map(int,input().split()))
res=[]
for i in a:
    l=0
    r=len(res)
    cres=-1
    while l<=r:
        mid=l+(r-l)//2
        if mid<len(res) and res[mid][-1]<i:
            r=mid-1
            cres=mid
        else:
            l=mid+1

    if cres!=-1:
        res[cres].append(i)
    else:
        res.append([i])

for i in range(len(res)):
    print(*res[i])
