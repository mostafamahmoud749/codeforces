def solve(indx,minv,cs,c):
    if indx>=len(a):
        if cs>=s and cs-minv<s:
            return c
        return -float("inf")


    ch1=solve(indx+1,min(minv,a[indx]),cs+a[indx],c+1)
    ch2=solve(indx+1,minv,cs,c)

    res=max(ch1,ch2)

    return res

t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))


    res=solve(0,float("inf"),0,0)
    # res=0
    # cs=0
    # i=0
    # j=0
    # while i<n-1:
        
    #     cs+=a[i]
    #     while cs-a[j]>=s:
    #         cs-=a[j]
    #         j+=1
    #     i+=1

    #     res=max(res,i-j)
            

    print(res) if res!=-float("inf") else print(0)