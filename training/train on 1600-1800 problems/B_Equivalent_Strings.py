import sys
sys.setrecursionlimit(200005)

def solve(a):
    if len(a)%2!=0:
        return a
    a1=solve(a[:len(a)//2])
    a2=solve(a[len(a)//2:])
    return a1+a2 if a1<a2 else a2+a1


a=list(input().strip())
b=list(input().strip())
print("YES") if solve(a)==solve(b) else print("NO")