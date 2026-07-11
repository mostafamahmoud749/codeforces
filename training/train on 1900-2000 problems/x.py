def solve(indx,a,b,c):
    if indx==10:
        if a==b==c==0:
            return 0
        else:
            return -float("inf")
    if dp[indx][a][b][c]!=-1:
        return dp[indx][a][b][c]
    

    cres=-float("inf")

    if a>0:
        if b>0:
            if c>0:
                cres=max(cres,1+solve(indx+1,a-1,b-1,c-1))
            cres=max(cres,solve(indx+1,a-1,b-1,c))
        if c>0:
            cres=max(cres,solve(indx+1,a-1,b,c-1))
            
        cres=max(cres,1+solve(indx+1,a-1,b,c))
    
    if b>0:
        if c>0:
            cres=max(cres,solve(indx+1,a,b-1,c-1))
        
        cres=max(cres,1+solve(indx+1,a,b-1,c))
    
    if c>0:
        cres=max(cres,1+solve(indx+1,a,b,c-1))
        
    cres=max(cres,solve(indx+1,a,b,c))

    dp[indx][a][b][c]=cres
    return cres


for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    ac=a.count("1")
    bc=b.count("1")
    cc=c.count("1")
    dp=[[[[-1]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    res=solve(0,ac,bc,cc)
    ans=[]
    for i in range(res):
        ans.append("1")
    for i in range(10-res):
        ans.append("0")
    print("".join(ans))