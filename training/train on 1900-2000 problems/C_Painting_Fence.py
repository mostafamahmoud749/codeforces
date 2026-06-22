import sys
sys.setrecursionlimit(5005)

def solve(l,r,h):
    ch1=r-l+1
    s=a[l]
    for i in range(l,r+1):
        s=min(s,a[i])
    ch2=s-h
    i=l
    for j in range(l,r+1):
        if a[j]==s:
            if i<=j-1: ch2+=solve(i,j-1,s)
            i=j+1
    if i<=r: ch2+=solve(i,r,s)
    return min(ch1,ch2)


n=int(input())
a=list(map(int,input().split()))
res=solve(0,n-1,0)
print(res)