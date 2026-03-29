t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    diff=0
    for i in range(1,n-1):
        cur_diff=abs(a[i]-a[i-1])+abs(a[i]-a[i+1])-abs(a[i-1]-a[i+1])
        if cur_diff>diff:
            diff=cur_diff
        s+=abs(a[i]-a[i-1])
    s+=abs(a[-1]-a[-2])
    print(min(s-abs(a[1]-a[0]),s-abs(a[-1]-a[-2]),s-diff))