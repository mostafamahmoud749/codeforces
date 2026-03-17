import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    last_el=math.ceil(s[0]/(n-k+1))

    tr=True
    for i in range(1,k):
        if s[i]-s[i-1]>=last_el:
            last_el=s[i]-s[i-1]
        else:
            tr=False
            break
    if tr==True:
        print("YES")
    else:
        print("NO")