import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
    n,x=LII()
    a=LII()

    c=(1<<40)-1
    res=0
    for i in a:
        if i&x==x:
            res+=1
            c&=i

    print(res) if res!=0 and c==x else print(-1)
