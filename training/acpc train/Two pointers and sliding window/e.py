t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    i=0
    j=n-1
    alice=a[i]
    bob=a[j]
    curindxs=[]
    while i<j:
        if alice==bob:
            curindxs=[i+1, n-j]
        if alice<=bob:
            i+=1
            if i==j: 
                break
            alice+=a[i]
        else:
            j-=1
            if i==j: 
                break
            bob+=a[j]
    if curindxs:
        print(curindxs[0]+curindxs[1])
    else:
        print(0)