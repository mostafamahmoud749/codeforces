# not solved

t= int(input())
for _ in range(t):
    n,h,k=map(int,input().split())
    bull=list(map(int,input().split()))
    sum=sum(bull)

    if h%sum==0:
        print((h//sum)+((h//sum)*k)-1)
    else:
        minsum=0
        sum=0
        index=0
        for i in range(n):
            sum+=bull[i]
            if sum>=h:
                index=i
                break
        
            
