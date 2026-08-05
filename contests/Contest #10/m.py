import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))



# if same values 1 and n

# if the space bettwen n and m even first element sum/2 end the sc the rest

# else -1


for _ in range(II()):
    n,m=LII()
    if n==0 and m==0:
        print(0)
    elif n==m:
        print(1,n)
    elif (n+m)%2==0:
        el1=(n+m)//2
        el2=n-el1
        print(2,el1,el2)
    else:
        print(-1)