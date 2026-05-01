t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=[0]*(n+1)
    p_max=[0]*(n+1)
    for i in range(n):
        p_max[i + 1] = max(p_max[i], a[i])
        p[i+1]=p[i]+a[i]
    ans=[]
    for k in range(1,n+1):
        if k==n:
            ans.append(p[n])
            continue
        k_sum=p[n]-p[n-k]
        o_max=p_max[n-k]
        f_k=a[n-k]
        imp=max(0,o_max-f_k)
        ans.append(imp+k_sum)
    print(' '.join(map(str, ans)))