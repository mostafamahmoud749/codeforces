import sys
sys.setrecursionlimit(100005)

def solve(indx):
    if indx<0:
        return 1
    if db[indx]!=-1:
        return db[indx]
    ch2=0
    ch1=solve(indx-1)
    if indx>=k:
        ch2=solve(indx-k)
    res=(ch1+ch2)%1000000007
    db[indx]=res
    return res

t,k=map(int,input().split())
db=[-1]*100005
maxr=0
q=[0]*t
for i in range(t):
    l,r=map(int,input().split())
    q[i]=[l,r]
    maxr=max(maxr,r)
p=[0]*(maxr+1)
for i in range(1,maxr+1):
    p[i]=(p[i-1]+solve(i))%1000000007
for i in range(len(q)):
    print((p[q[i][1]]-p[q[i][0]-1])%1000000007)