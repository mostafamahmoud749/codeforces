t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    
    for i in range(n):
        a[i]=[a[i],i+1]
    
    a.sort()
    print(a)