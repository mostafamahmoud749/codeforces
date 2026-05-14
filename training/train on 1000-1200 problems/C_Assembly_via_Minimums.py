t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    b.sort()
    a=[]
    j=n-1
    i=0
    s=0
    while i<n-1:
        a.append(b[s])
        s+=j
        j-=1
        i+=1
    a.append(10**9)
    print(*a)