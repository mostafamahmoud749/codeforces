# t=int(input())
# for _ in range(t):
#     n,q=map(int,input().split())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     asum=[]
#     for j in range(q):
#         l,r=map(int,input().split())
#         l-=1
#         r-=1
#         res=0
#         bigestmax=0
#         if n-1>=r+1:
#             bigestmax=max(b[r+1],a[r+1])
#         for i in range(r,l-1,-1):
#             bigestmax=max(bigestmax,b[i],a[i])
#             res+=bigestmax
#         asum.append(res)

#     print(*asum)

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    asum = []
    for j in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        res = 0
        max_b = 0
        if n-1>=r+1:
            max_b=b[r+1]
        for i in range(r, l - 1, -1):
            max_b = max(max_b, b[i])
            res += max(a[i], max_b)
        asum.append(res)
    print(*asum)
