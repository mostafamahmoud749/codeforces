t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(map(int,input().split()))
    m=0
    cur_m=0
    for i in range(n-1):
        if a[i]==a[i+1]-1:
            cur_m+=1
        elif a[i]==a[i+1]:
            continue
        else:
            m=max(m,cur_m)
            cur_m=0
    m=max(m,cur_m)
    print(m+1)
