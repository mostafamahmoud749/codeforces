n=int(input())
a=list(map(int,input().split()))
sa=a.copy()
sa.sort()
r=n-1
l=0
if sa==a:
    print("yes")
    print("1 1")
else:
    while sa[l]==a[l]:
        l+=1
    while sa[r]==a[r]:
        r-=1
    a[l:r+1]=reversed(a[l:r+1])
    if sa==a:
        print("yes")
        print(l+1,r+1)
    else:
        print("no")