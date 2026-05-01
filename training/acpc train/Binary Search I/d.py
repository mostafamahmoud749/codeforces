t=int(input())
for _ in range(t):
    d=int(input())
    l=0
    r=d/2
    res=-1
    if d==0:
        print("Y 0.000000000 0.000000000")
        continue
    elif d<4:
        print("N")
        continue
    while r-l>=1e-10:
        mid=l+(r-l)/2
        if mid*(d-mid)>d:
            r=mid
        else:
            l=mid
    print(f"Y {d-l:.9f} {l:.9f}")