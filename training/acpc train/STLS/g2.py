from collections import deque

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=sorted(map(int,input().split()))

    cur_el=a[0]
    diff_indxs=deque()
    p=[0]*(n+1)
    p[0]=1
    start=0
    max_res=1

    for i in range(1,n):
        if cur_el==a[i]:
            p[i]=i-start+1
        elif a[i]==cur_el+1:
            cur_el=a[i]
            diff_indxs.append(i-1)
            while len(diff_indxs)>=k:
                start=diff_indxs.popleft()+1
            p[i]=i-start+1
        else:
            cur_el=a[i]
            diff_indxs=deque()
            start=i
            p[i]=1
        max_res=max(p[i],max_res)

    print(max_res)