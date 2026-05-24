import sys
sys.setrecursionlimit(10**8)

def calc(aindx,bindx):
    if aindx+bindx==len(c):
        return 0
    if db[aindx][bindx]!=-1:
        return db[aindx][bindx]

    ch1=float("inf")
    ch2=float("inf")
    if aindx<len(a):
        ch1=calc(aindx+1,bindx)
        if a[aindx]!=c[aindx+bindx]:
            ch1+=1
    if bindx<len(b):
        ch2=calc(aindx,bindx+1)
        if b[bindx]!=c[aindx+bindx]:
            ch2+=1
    
    res=min(ch1,ch2)
    db[aindx][bindx]=res
    return res

t=int(input())
for _ in range(t):
    a=list(input().strip())
    b=list(input().strip())
    c=list(input().strip())
    db = [[-1] * (len(b)+1) for _ in range(len(a)+1)]
    res=calc(0,0)
    print(res)