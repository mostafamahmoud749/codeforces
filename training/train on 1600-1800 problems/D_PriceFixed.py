n=int(input())
items=[]
for _ in range(n):
    a,b=map(int,input().split())
    items.append([b,a])
items.sort()
l=0
r=n-1
c=0
res=0
while l<=r:
    if c>=items[l][0]:
        res+=items[l][1]
        c+=items[l][1]
        l+=1
    else:
        if items[r][1]<=0:
            r-=1
            continue
        take=min(items[r][1],items[l][0]-c)
        items[r][1]-=take
        c+=take
        res+=2*take
print(res)