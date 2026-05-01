def can(mid):
    curr=rubles
    for i in range(3):
        amount=mid*req[i]
        if amount>ing[i]:
            curr-=(amount-ing[i])*pri[i]
    if curr<0:
        return False
    else:
        return True
S=input()
ing=list(map(int,input().split()))
pri=list(map(int,input().split()))
rubles=int(input())
req=[0]*3
for i in S:
    if i=="B":
        req[0]+=1
    elif i=="S":
        req[1]+=1
    else:
        req[2]+=1
l=0
r=10**13
res=0
while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        res=mid
        l=mid+1
    else:
        r=mid-1
print(res)