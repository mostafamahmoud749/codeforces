t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in range(n): 
        for j in range(i,n):
            if a[j]-a[i]==j-i and i<j:
                res+=1
    print(res)