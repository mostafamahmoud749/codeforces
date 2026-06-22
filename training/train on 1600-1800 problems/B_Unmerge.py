def solve(la,lb,ac):
    curindx=max(la,lb)+1
    if ac>n/2 or (curindx-1)-ac>2: return False
    if curindx==n:
        if ac==n/2:
            return True
    return False




t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dp=[[-1]*(n+1) for _ in range(n+1)]
    print(solve(0,-1,0,0))