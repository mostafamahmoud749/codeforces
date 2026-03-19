t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l_m=[0]*n
    l_m[0] = a[0] + 0
    for i in range(1,n):
        l_m[i] = max(l_m[i-1], a[i]+i)
        
    r_m=[0]*n
    r_m[n-1] = a[n-1] - (n-1)
    for i in range(n-2,-1,-1):
        r_m[i] = max(r_m[i+1], a[i]-i)
        
    ans=-float('inf')
    for i in range(1, n-1):
        cur = l_m[i-1] + a[i] + r_m[i+1]
        if cur>ans:
            ans=cur
    print(ans)
