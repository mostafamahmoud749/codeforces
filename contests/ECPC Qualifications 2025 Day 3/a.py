import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve(a,b,o):
    if o=="/":
        return a//b
    if o=="+":
        return a+b
    elif o=="*":
        return a*b
    else:
        return a-b

a=list(input().split())
x=int(a[0])
y=int(a[2])
z=int(a[4])

p1=a[1]
p2=a[3]

res=0
if (p2=="*" or p2=="/") and (p1=="+" or p1=="-"):
    cur=solve(y,z,p2)
    res=solve(x,cur,p1)
else:
    cur=solve(x,y,p1)
    res=solve(cur,z,p2)
    
print(res)