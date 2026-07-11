from collections import deque

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=1
    curk=1
    nextk=0

    i=1
    j=1
    while i<n-1:
        i+=1

        if a[i]<a[i-1]:
            curk-=1
            nextk+=i-j
            j=i
        
        if curk==0:
            curk=nextk
            nextk=0
            res+=1
    
    print(res)