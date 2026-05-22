def genrate(indx,c):
    if indx==lna:
        p.add(int(c))
        return
    if c!="" and c!=a[:indx]:
        p.add(int(c+min(nums)*(lna-indx)))
        p.add(int(c+max(nums)*(lna-indx)))
        return
    for i in range(len(nums)):
        genrate(indx+1,c+nums[i])

t=int(input())
for _ in range(t):
    a,n=map(str,input().split())
    lna=len(a)
    n=int(n)
    nums=list(map(str,input().split()))
    p=set()
    genrate(0,"")
    if lna>1:
        p.add(max(nums)*(lna-1))
    if nums[0]=='0' and len(nums)>1:
        p.add(nums[1]+nums[0]*lna)
    p.add(min(nums)*(lna+1))
    res=float("inf")
    for i in p:
        res=min(res,abs(int(a)-int(i)))
    print(res)