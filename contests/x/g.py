t=int(input())
for _ in range(t):
    h1,h2,b=map(int,input().split())

    # res=1
    # i=1
    # while True:
    #     if h1*(((b-1)/b)**i)<=h2:
    #         break
    #     i+=1
    # print(i)

    r=100000000000
    l=1
    res=0
    while l<=r:
        mid=l+(r-l)//2
        if h1*(((b-1)/b)**mid)<=h2:
            r=mid-1
            res=mid
        else:
            l=mid+1
    print(res)