def split(n):
    global s
    if n==m:
        s=True
    else:
        if int(n*(2/3))+int(n*(1/3))==n:
            split(int(n*(2/3)))    
            split(int(n*(1/3))) 


t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=False
    split(n)
    if s:
        print("yes")
    else:
        print("no")