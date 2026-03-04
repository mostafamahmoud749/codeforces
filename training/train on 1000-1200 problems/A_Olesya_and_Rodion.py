n,t=map(int,input().split())
lent=len(str(t))
if lent>n:
    print(-1)
elif n==lent:
    print(t)
else:
    print(str(t)+str("0"*(n-lent)))