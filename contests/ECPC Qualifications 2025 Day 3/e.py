import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()
for _ in range(t):
    n,l=LII()
    res=0
    cur=1
    c=0
    while True:
        if c==0:
            if (cur<<1)<=l:
                cur=cur<<1
                res+=1
            else:
                break
        if c==1:
            if ((cur<<1)|1)<=l:
                cur=(cur<<1)|1
                res+=1
            else:
                break
        c=1-c


    print("YES") if res>=n else print("NO")