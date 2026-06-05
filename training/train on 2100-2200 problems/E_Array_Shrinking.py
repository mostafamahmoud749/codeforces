def solve(indx):
    if indx>=len(a)-1:
        return len(a)
    if dp[indx]!=-1:
        return dp[indx]
    ch1=float("inf")
    ch2=float("inf")
    ch3=float("inf")
    if a[indx]==a[indx+1]:
        i=a.pop(indx+1)
        a[indx]+=1
        ch1=solve(indx)
        a[indx]-=1
        a.insert(indx+1,i)
    if indx>0 and a[indx-1]==a[indx]:
        i=a.pop(indx-1)
        ch2=solve(indx-1)
        a.insert(indx-1,i)
    ch3=solve(indx+1)
    res=min(ch1,ch2,ch3)
    dp[indx]=res
    return res


n=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(n)]
res=solve(0)
print(res)