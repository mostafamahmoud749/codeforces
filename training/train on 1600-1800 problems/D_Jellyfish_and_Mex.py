def solve(cmex):
    if cmex==0:
        return 0
    if cmex in dp:
        return dp[cmex]
    res=float("inf")
    for i in range(cmex):
        res=min(res,((freq[i]-1)*cmex)+i+solve(i))
    dp[cmex]=res
    return res


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    freq={}
    dp={}
    for i in a:
        freq[i]=freq.get(i,0)+1
    mex=0
    m=set(a)
    while mex in m:
        mex+=1
    res=solve(mex)
    print(res)

# 0 1 2 3
# 3 2 1 0

# 