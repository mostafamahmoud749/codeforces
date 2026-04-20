t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1: 
        print(-1) 
        continue
    seen=set()
    res=float('inf')
    i=0
    j=0
    while i<n:
        if a[i] not in seen:
            seen.add(a[i])
            i+=1
        else:
            while a[i] in seen:
                res=min(res,i-j)
                seen.remove(a[j])
                j+=1
    print(res+1) if res!=float('inf')else print(-1)