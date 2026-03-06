t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    oddsum=0
    evensum=0
    for i in range(n):
        if a[i]%2==0:
            evensum+=1
        else:
            oddsum+=1
    