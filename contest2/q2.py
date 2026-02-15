from math import ceil


t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    max=nums[0]
    l=0
    
    for i in range(1,(n//2)+1):
        if min(nums[i-1],nums[(i*2)-1])>=max:
            max=min(nums[i-1],nums[(i*2)-1])
            l+=1
        else:
            print("NO")
            break
    if n%2!=0 and l==(n//2):
        if nums[(n//2)]>=max:
            print("YES")
        else:
            print("NO")
    elif l==(n//2):
        print("YES")
    else:
        print("NO")
    