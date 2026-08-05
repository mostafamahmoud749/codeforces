import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()
for _ in range(t):
    n,k,m=LII()

    res=1
    prev=-1
    for o in range(m):
        id,time=input().split()
        # id=x[0]
        # time=x[2:] 
        minutes=(int(time[0:2])*60)+int(time[3:])
        # print(minutes)
        if prev!=-1 and abs(minutes-prev)>k:
            res+=1
        prev=minutes
    print(res)

